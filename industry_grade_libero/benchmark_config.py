#!/usr/bin/env python3
"""Shared configuration helpers for the multi-GPU VLA-0 LIBERO benchmark."""

from __future__ import annotations

import os
import re
import sys
from pathlib import Path
from typing import Iterable


DEFAULT_MODES = ["bf16", "int8", "nf4"]
DEFAULT_SUITES = ["libero_spatial", "libero_object", "libero_goal", "libero_10"]
DEFAULT_SEED = 7
DEFAULT_ACTION_HORIZON = 1
DEFAULT_ENSEMBLE_PREDICTION = 8
DEFAULT_TASK_ID_COUNT = 10
DEFAULT_MAX_WORKERS_PER_GPU = 1
TOTAL_LIBERO_INIT_STATES = 50


STATIC_TASKS = {
    "libero_spatial": [
        "pick_up_the_black_bowl_on_the_ramekin_and_place_it_on_the_plate",
        "pick_up_the_black_bowl_on_the_cookie_box_and_place_it_on_the_plate",
        "pick_up_the_black_bowl_between_the_plate_and_the_ramekin_and_place_it_on_the_plate",
        "pick_up_the_black_bowl_next_to_the_plate_and_place_it_on_the_plate",
        "pick_up_the_black_bowl_on_the_stove_and_place_it_on_the_plate",
        "pick_up_the_black_bowl_from_table_center_and_place_it_on_the_plate",
        "pick_up_the_black_bowl_in_the_top_drawer_of_the_wooden_cabinet_and_place_it_on_the_plate",
        "pick_up_the_black_bowl_next_to_the_cookie_box_and_place_it_on_the_plate",
        "pick_up_the_black_bowl_next_to_the_ramekin_and_place_it_on_the_plate",
        "pick_up_the_black_bowl_on_the_wooden_cabinet_and_place_it_on_the_plate",
    ],
    "libero_object": [
        "pick_up_the_alphabet_soup_and_place_it_in_the_basket",
        "pick_up_the_tomato_sauce_and_place_it_in_the_basket",
        "pick_up_the_butter_and_place_it_in_the_basket",
        "pick_up_the_cream_cheese_and_place_it_in_the_basket",
        "pick_up_the_bbq_sauce_and_place_it_in_the_basket",
        "pick_up_the_salad_dressing_and_place_it_in_the_basket",
        "pick_up_the_chocolate_pudding_and_place_it_in_the_basket",
        "pick_up_the_milk_and_place_it_in_the_basket",
        "pick_up_the_orange_juice_and_place_it_in_the_basket",
        "pick_up_the_ketchup_and_place_it_in_the_basket",
    ],
    "libero_goal": [
        "put_the_bowl_on_the_stove",
        "put_the_wine_bottle_on_top_of_the_cabinet",
        "turn_on_the_stove",
        "put_the_cream_cheese_in_the_bowl",
        "open_the_middle_drawer_of_the_cabinet",
        "put_the_wine_bottle_on_the_rack",
        "push_the_plate_to_the_front_of_the_stove",
        "put_the_bowl_on_the_plate",
        "put_the_bowl_on_top_of_the_cabinet",
        "open_the_top_drawer_and_put_the_bowl_inside",
    ],
    "libero_10": [
        "KITCHEN_SCENE8_put_both_moka_pots_on_the_stove",
        "LIVING_ROOM_SCENE1_put_both_the_alphabet_soup_and_the_cream_cheese_box_in_the_basket",
        "LIVING_ROOM_SCENE2_put_both_the_alphabet_soup_and_the_tomato_sauce_in_the_basket",
        "KITCHEN_SCENE3_turn_on_the_stove_and_put_the_moka_pot_on_it",
        "LIVING_ROOM_SCENE5_put_the_white_mug_on_the_left_plate_and_put_the_yellow_and_white_mug_on_the_right_plate",
        "KITCHEN_SCENE4_put_the_black_bowl_in_the_bottom_drawer_of_the_cabinet_and_close_it",
        "KITCHEN_SCENE6_put_the_yellow_and_white_mug_in_the_microwave_and_close_it",
        "STUDY_SCENE1_pick_up_the_book_and_place_it_in_the_back_compartment_of_the_caddy",
        "LIVING_ROOM_SCENE2_put_both_the_cream_cheese_box_and_the_butter_in_the_basket",
        "LIVING_ROOM_SCENE6_put_the_white_mug_on_the_plate_and_put_the_chocolate_pudding_to_the_right_of_the_plate",
    ],
}


def safe_name(value: str, max_len: int = 120) -> str:
    """Return a filesystem-safe but readable name."""
    safe = re.sub(r"[^A-Za-z0-9_.-]+", "_", value).strip("_")
    safe = re.sub(r"_+", "_", safe)
    return safe[:max_len] if len(safe) > max_len else safe


def add_vla0_paths(vla0_root: Path) -> None:
    """Add likely VLA-0, RoboVerse, LeRobot, and LIBERO paths to sys.path."""
    vla0_root = vla0_root.resolve()
    candidates = [
        vla0_root,
        vla0_root / "libs" / "RoboVerse",
        vla0_root / "libs" / "RoboVerse" / "libs" / "lerobot" / "src",
        vla0_root / "libs" / "LIBERO",
        vla0_root.parent / "LIBERO",
        vla0_root.parent / "LIBERO" / "libero",
        Path(os.environ.get("LIBERO_ROOT", "")),
    ]
    for candidate in candidates:
        if candidate and candidate.exists():
            text = str(candidate)
            if text not in sys.path:
                sys.path.insert(0, text)


def discover_tasks(vla0_root: Path, suites: Iterable[str]) -> dict[str, list[str]]:
    """Discover task names from the installed LIBERO package, with a static fallback."""
    add_vla0_paths(vla0_root)
    selected = list(suites)
    try:
        from libero.libero import benchmark

        discovered = {}
        benchmark_dict = benchmark.get_benchmark_dict()
        for suite in selected:
            task_suite = benchmark_dict[suite]()
            discovered[suite] = [task.name for task in task_suite.tasks]
        return discovered
    except Exception:
        return {suite: list(STATIC_TASKS[suite]) for suite in selected}


def expected_episode_count(task_id_count: int) -> int:
    if TOTAL_LIBERO_INIT_STATES % task_id_count != 0:
        raise ValueError(
            f"task_id_count={task_id_count} must divide {TOTAL_LIBERO_INIT_STATES}"
        )
    return TOTAL_LIBERO_INIT_STATES // task_id_count

