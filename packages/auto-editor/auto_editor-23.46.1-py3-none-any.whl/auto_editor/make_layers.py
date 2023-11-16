from __future__ import annotations

import os
from fractions import Fraction
from typing import TYPE_CHECKING, Any, NamedTuple

import numpy as np

from auto_editor.analyze import FileSetup, Levels
from auto_editor.ffwrapper import FFmpeg, FileInfo, initFileInfo
from auto_editor.lang.palet import Lexer, Parser, env, interpret, is_boolarr
from auto_editor.lib.data_structs import print_str
from auto_editor.lib.err import MyError
from auto_editor.timeline import (
    ALayer,
    ASpace,
    TlAudio,
    TlVideo,
    VLayer,
    VSpace,
    audio_objects,
    v1,
    v3,
    visual_objects,
)
from auto_editor.utils.chunks import Chunks, chunkify, chunks_len, merge_chunks
from auto_editor.utils.cmdkw import ParserError, parse_with_palet
from auto_editor.utils.func import mut_margin
from auto_editor.utils.types import Args, CoerceError, time

if TYPE_CHECKING:
    from numpy.typing import NDArray

    from auto_editor.output import Ensure
    from auto_editor.utils.bar import Bar
    from auto_editor.utils.log import Log

    BoolList = NDArray[np.bool_]


class Clip(NamedTuple):
    start: int
    dur: int
    offset: int
    speed: float
    src: str


def clipify(chunks: Chunks, src: str, start: int = 0) -> list[Clip]:
    clips: list[Clip] = []
    i = 0
    for chunk in chunks:
        if chunk[2] != 99999:
            dur = round((chunk[1] - chunk[0]) / chunk[2])
            if dur == 0:
                continue

            offset = chunk[0]

            if not (clips and clips[-1].start == round(start)):
                clips.append(Clip(start, dur, offset, chunk[2], src))
            start += dur
            i += 1

    return clips


def make_av(
    all_clips: list[list[Clip]], sources: dict[str, FileInfo], _inputs: list[int]
) -> tuple[VSpace, ASpace]:
    if len(_inputs) > 1000:
        raise ValueError("Number of file inputs can't be greater than 1000")

    inputs = [str(i) for i in _inputs]
    vtl: VSpace = []
    atl: ASpace = [[] for _ in range(max(len(sources[i].audios) for i in inputs))]

    for clips, inp in zip(all_clips, inputs):
        src = sources[inp]

        for c in clips:
            if src.videos:
                if len(vtl) == 0:
                    vtl.append([])
                vtl[0].append(TlVideo(c.start, c.dur, c.src, c.offset, c.speed, 0))

        for c in clips:
            for a in range(len(src.audios)):
                atl[a].append(TlAudio(c.start, c.dur, c.src, c.offset, c.speed, 1, a))

    return vtl, atl


def run_interpreter_for_edit_option(
    text: str, filesetup: FileSetup
) -> NDArray[np.bool_]:
    ensure = filesetup.ensure
    src = filesetup.src
    tb = filesetup.tb
    bar = filesetup.bar
    temp = filesetup.temp
    log = filesetup.log

    try:
        parser = Parser(Lexer("`--edit`", text))
        if log.is_debug:
            log.debug(f"edit: {parser}")

        env["timebase"] = filesetup.tb
        env["@levels"] = Levels(ensure, src, tb, bar, temp, log)
        env["@filesetup"] = filesetup

        results = interpret(env, parser)

        if len(results) == 0:
            raise MyError("Expression in --edit must return a bool-array, got nothing")

        result = results[-1]
        if callable(result):
            result = result()

        if not is_boolarr(result):
            raise MyError(
                f"Expression in --edit must return a bool-array, got {print_str(result)}"
            )
    except MyError as e:
        log.error(e)

    assert isinstance(result, np.ndarray)
    return result


def make_timeline(
    sources: dict[str, FileInfo],
    inputs: list[int],
    ffmpeg: FFmpeg,
    ensure: Ensure,
    args: Args,
    sr: int,
    bar: Bar,
    temp: str,
    log: Log,
) -> v3:
    inp = None if not inputs else sources[str(inputs[0])]

    if inp is None:
        tb, res = Fraction(30), (1920, 1080)
    else:
        tb = inp.get_fps() if args.frame_rate is None else args.frame_rate
        res = inp.get_res() if args.resolution is None else args.resolution

    chunks, vclips, aclips = make_layers(
        sources,
        inputs,
        ensure,
        tb,
        args.edit_based_on,
        args.margin,
        args.cut_out,
        args.add_in,
        args.mark_as_silent,
        args.mark_as_loud,
        args.set_speed_for_range,
        args.silent_speed,
        args.video_speed,
        bar,
        temp,
        log,
    )

    for raw in args.source:
        exploded = raw.split(":")
        if len(exploded) != 2:
            log.error("source label:path must have one :")
        label, path = exploded
        if len(label) > 55:
            log.error("Label must not exceed 55 characters.")

        for ill_char in ",.;()/\\[]}{'\"|#&<>^%$=@ ":
            if ill_char in label:
                log.error(f"Label '{label}' contains illegal character: {ill_char}")

        if label[0] in "0123456789":
            log.error(f"Label '{label}' must not start with a digit")
        if label[0] == "-":
            log.error(f"Label '{label}' must not start with a dash")

        if not os.path.isfile(path):
            log.error(f"Path '{path}' is not a file")

        sources[label] = initFileInfo(path, ffmpeg, log, label)

    v1_compatiable = None if inp is None else v1(inp, chunks)
    tl = v3(sources, tb, sr, res, args.background, vclips, aclips, v1_compatiable)

    w, h = res
    pool: VLayer = []
    apool: ALayer = []

    env["start"] = 0
    env["end"] = tl.end

    for obj_attrs_str in args.add:
        exploded = obj_attrs_str.split(":", 1)
        obj_s = exploded[0]
        attrs = "" if len(exploded) == 1 else exploded[1]

        try:
            if obj_s in visual_objects:
                dic_obj = parse_with_palet(attrs, visual_objects[obj_s][1], env)
                pool.append(visual_objects[obj_s][0](**dic_obj))
            elif obj_s in audio_objects:
                dic_obj = parse_with_palet(attrs, audio_objects[obj_s][1], env)
                apool.append(audio_objects[obj_s][0](**dic_obj))
            else:
                log.error(f"Unknown timeline object: '{obj_s}'")
        except (ParserError, CoerceError) as e:
            log.error(e)

    for vobj in pool:
        tl.v.append([vobj])

    for aobj in apool:
        tl.a.append([aobj])

    return tl


def make_layers(
    sources: dict[str, FileInfo],
    inputs: list[int],
    ensure: Ensure,
    tb: Fraction,
    method: str,
    margin: tuple[str, str],
    cut_out: list[list[str]],
    add_in: list[list[str]],
    mark_silent: list[list[str]],
    mark_loud: list[list[str]],
    speed_ranges: list[tuple[float, str, str]],
    silent_speed: float,
    loud_speed: float,
    bar: Bar,
    temp: str,
    log: Log,
) -> tuple[Chunks, VSpace, ASpace]:
    start = 0
    all_clips: list[list[Clip]] = []
    all_chunks: list[Chunks] = []

    try:
        start_margin = time(margin[0], tb)
        end_margin = time(margin[1], tb)
    except CoerceError as e:
        log.error(e)

    speed_map = [silent_speed, loud_speed]
    speed_hash = {
        0: silent_speed,
        1: loud_speed,
    }

    def get_speed_index(speed: float) -> int:
        if speed in speed_map:
            return speed_map.index(speed)
        speed_map.append(speed)
        speed_hash[len(speed_map) - 1] = speed
        return len(speed_map) - 1

    def parse_time(val: str, arr: NDArray) -> int:
        if val == "start":
            return 0
        if val == "end":
            return len(arr)
        try:
            num = time(val, tb)
            return num if num >= 0 else num + len(arr)
        except CoerceError as e:
            log.error(e)

    def mut_set_range(arr: NDArray, _ranges: list[list[str]], index: Any) -> None:
        for _range in _ranges:
            assert len(_range) == 2
            pair = [parse_time(val, arr) for val in _range]
            arr[pair[0] : pair[1]] = index

    for i in map(str, inputs):
        filesetup = FileSetup(sources[i], ensure, len(inputs) < 2, tb, bar, temp, log)
        has_loud = run_interpreter_for_edit_option(method, filesetup)

        if len(mark_loud) > 0:
            mut_set_range(has_loud, mark_loud, loud_speed)

        if len(mark_silent) > 0:
            mut_set_range(has_loud, mark_silent, silent_speed)

        mut_margin(has_loud, start_margin, end_margin)

        # Setup for handling custom speeds
        has_loud = has_loud.astype(np.uint)

        try:
            if len(cut_out) > 0:
                # always cut out even if 'silent_speed' is not 99,999
                mut_set_range(has_loud, cut_out, get_speed_index(99_999))

            if len(add_in) > 0:
                # set to 'video_speed' index
                mut_set_range(has_loud, add_in, 1)

            for speed_range in speed_ranges:
                speed = speed_range[0]
                _range = list(speed_range[1:])
                mut_set_range(has_loud, [_range], get_speed_index(speed))
        except CoerceError as e:
            log.error(e)

        chunks = chunkify(has_loud, speed_hash)

        all_chunks.append(chunks)
        all_clips.append(clipify(chunks, i, start))
        start += round(chunks_len(chunks))

    vclips, aclips = make_av(all_clips, sources, inputs)

    return merge_chunks(all_chunks), vclips, aclips
