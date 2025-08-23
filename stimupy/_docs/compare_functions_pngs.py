#!/usr/bin/env python3
"""
Script to compare stimupy functions with generated PNG files.

This script identifies:
1. Functions that don't have corresponding PNG files
2. PNG files that don't correspond to actual functions
3. Naming mismatches between functions and PNG files
"""

import inspect
import sys
from pathlib import Path

# Add the stimupy package to the path
stimupy_root = Path(__file__).parents[2]
sys.path.insert(0, str(stimupy_root))

import stimupy


def get_all_stimupy_functions():
    """Get all stimulus-generating functions from stimupy."""
    functions = set()

    # Helper function to check if a function is a stimulus generator
    def is_stimulus_function(obj, module_name):
        if not callable(obj):
            return False
        if obj.__name__.startswith("_"):
            return False
        if obj.__name__ in ["overview", "plot_overview"]:
            return False
        # Skip utility functions that don't generate stimuli
        if obj.__name__ in [
            "mask_angle",
            "mask_segments",
            "mask_frames",
            "mask_rings",
            "resolve_grating_params",
            "round_n_phases",
            "add_targets",
            "extend_target_idx",
            "mask_from_idx",
            "resolve_cells_1d",
            "resolve_dungeon_params",
            "add_waves",
        ]:
            return False
        # Must have the module in its __module__ to avoid imported functions
        if hasattr(obj, "__module__") and obj.__module__:
            return module_name in obj.__module__
        return True

    # Components
    for module_name in stimupy.components.__all__:
        if module_name == "overview":
            continue
        try:
            module = getattr(stimupy.components, module_name)
            for name in dir(module):
                obj = getattr(module, name)
                if is_stimulus_function(obj, module_name):
                    functions.add(f"components.{module_name}.{name}")
        except AttributeError:
            continue

    # Stimuli
    for module_name in stimupy.stimuli.__all__:
        if module_name == "overview":
            continue
        try:
            module = getattr(stimupy.stimuli, module_name)
            for name in dir(module):
                obj = getattr(module, name)
                if is_stimulus_function(obj, module_name):
                    functions.add(f"stimuli.{module_name}.{name}")
        except AttributeError:
            continue

    # Noises
    for module_name in stimupy.noises.__all__:
        if module_name == "overview":
            continue
        try:
            module = getattr(stimupy.noises, module_name)
            for name in dir(module):
                obj = getattr(module, name)
                if is_stimulus_function(obj, module_name):
                    functions.add(f"noises.{module_name}.{name}")
        except AttributeError:
            continue

    return functions


def get_generated_pngs():
    """Get list of generated PNG files (without .png extension)."""
    png_dir = stimupy_root / "docs" / "_static" / "generated_stimuli"
    if not png_dir.exists():
        return set()

    png_files = set()
    for png_file in png_dir.glob("*.png"):
        # Remove .png extension to get the function name
        png_files.add(png_file.stem)

    return png_files


def compare_functions_and_pngs():
    """Compare stimupy functions with generated PNG files."""
    print("Analyzing stimupy functions and generated PNG files...")
    print("=" * 60)

    # Get all functions and PNGs
    all_functions = get_all_stimupy_functions()
    generated_pngs = get_generated_pngs()

    # Find discrepancies
    missing_pngs = all_functions - generated_pngs
    extra_pngs = generated_pngs - all_functions
    matching = all_functions & generated_pngs

    print(f"\n📊 SUMMARY")
    print(f"Total stimupy functions: {len(all_functions)}")
    print(f"Generated PNG files: {len(generated_pngs)}")
    print(f"Perfect matches: {len(matching)}")
    print(f"Missing PNGs: {len(missing_pngs)}")
    print(f"Extra PNGs: {len(extra_pngs)}")
    print(f"Coverage: {len(matching) / len(all_functions) * 100:.1f}%")

    if missing_pngs:
        print(f"\n❌ MISSING PNGs ({len(missing_pngs)} functions without images):")
        print("These functions exist but don't have corresponding PNG files:")
        for func in sorted(missing_pngs):
            print(f"  - {func}")

    if extra_pngs:
        print(f"\n❓ EXTRA PNGs ({len(extra_pngs)} images without matching functions):")
        print("These PNG files don't correspond to actual stimupy functions:")
        for png in sorted(extra_pngs):
            print(f"  - {png}")

    if not missing_pngs and not extra_pngs:
        print(f"\n✅ PERFECT MATCH!")
        print("All stimupy functions have corresponding PNG files with correct names.")

    print(f"\n📁 PNG files are located in: {Path(__file__).parent / 'generated_stimuli'}")

    return {
        "total_functions": len(all_functions),
        "generated_pngs": len(generated_pngs),
        "matching": len(matching),
        "missing": len(missing_pngs),
        "extra": len(extra_pngs),
        "coverage": len(matching) / len(all_functions) * 100,
        "missing_list": sorted(missing_pngs),
        "extra_list": sorted(extra_pngs),
    }


def print_function_lists():
    """Print detailed lists of all functions and PNGs for debugging."""
    all_functions = get_all_stimupy_functions()
    generated_pngs = get_generated_pngs()

    print(f"\n🔍 DETAILED LISTS")
    print("=" * 60)

    print(f"\nAll stimupy functions ({len(all_functions)}):")
    for func in sorted(all_functions):
        print(f"  {func}")

    print(f"\nGenerated PNG files ({len(generated_pngs)}):")
    for png in sorted(generated_pngs):
        print(f"  {png}")


if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser(
        description="Compare stimupy functions with generated PNG files"
    )
    parser.add_argument(
        "--detailed", action="store_true", help="Print detailed lists of all functions and PNGs"
    )
    args = parser.parse_args()

    # Run the comparison
    results = compare_functions_and_pngs()

    # Print detailed lists if requested
    if args.detailed:
        print_function_lists()
