#!/usr/bin/env python3
"""
Script to generate stimulus images using default parameters from the params package.

This script discovers all parameter classes, generates stimuli using their default values,
and saves the results as PNG images.
"""

import sys
from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np

# Add the stimupy package to the path
stimupy_root = Path(__file__).parent.parent.parent
sys.path.insert(0, str(stimupy_root))

# Add the current directory to import params
sys.path.insert(0, str(Path(__file__).parent))

import stimupy
from stimupy import papers


def get_all_param_classes():
    """Get all parameter classes from the params package."""
    param_classes = {}

    # Import the params modules
    try:
        import params.components as components
        import params.noises as noises
        import params.stimuli as param_stimuli

        # Process components
        for module_name in components.__all__:
            module = getattr(components, module_name)
            if hasattr(module, "__all__"):
                for class_name in module.__all__:
                    param_class = getattr(module, class_name)
                    if hasattr(param_class, "get_stimulus_params"):
                        # Convert class name to function name
                        func_name = class_name.replace("Params", "").lower()
                        key = f"components.{module_name}.{func_name}"
                        param_classes[key] = param_class

        # Process stimuli
        for module_name in param_stimuli.__all__:
            module = getattr(param_stimuli, module_name)
            if hasattr(module, "__all__"):
                for class_name in module.__all__:
                    param_class = getattr(module, class_name)
                    if hasattr(param_class, "get_stimulus_params"):
                        # Convert class name to function name
                        func_name = class_name.replace("Params", "")
                        # Handle special naming cases before converting to lowercase
                        if func_name.endswith("Generalized"):
                            func_name = func_name.replace("Generalized", "")
                            # Convert to snake_case first, then add _generalized
                            import re

                            func_name = re.sub("([a-z0-9])([A-Z])", r"\1_\2", func_name).lower()
                            if func_name:  # If there's a prefix, add underscore
                                func_name = func_name + "_generalized"
                            else:  # If it's just "Generalized", use "generalized"
                                func_name = "generalized"
                        elif func_name.endswith("Rectangles"):
                            func_name = func_name.replace("Rectangles", "_rectangles").lower()
                        elif func_name.endswith("Triangles"):
                            func_name = func_name.replace("Triangles", "_triangles").lower()
                        elif func_name.endswith("TwoSided"):
                            func_name = func_name.replace("TwoSided", "")
                            # Convert to snake_case first, then add _two_sided
                            import re

                            func_name = re.sub("([a-z0-9])([A-Z])", r"\1_\2", func_name).lower()
                            if func_name:  # If there's a prefix, add underscore
                                func_name = func_name + "_two_sided"
                            else:  # If it's just "TwoSided", use "two_sided"
                                func_name = "two_sided"
                        else:
                            # Convert camelCase to snake_case for other cases
                            import re

                            func_name = re.sub("([a-z0-9])([A-Z])", r"\1_\2", func_name).lower()

                        key = f"stimuli.{module_name}.{func_name}"
                        param_classes[key] = param_class

        # Process noises (now structured like components and stimuli)
        for module_name in noises.__all__:
            module = getattr(noises, module_name)
            if hasattr(module, "__all__"):
                for class_name in module.__all__:
                    param_class = getattr(module, class_name)
                    if hasattr(param_class, "get_stimulus_params"):
                        # Convert class name to function name
                        func_name = class_name.replace("Params", "")
                        # Handle special naming cases
                        if func_name == "OneOverF":
                            func_name = "one_over_f"
                        else:
                            func_name = func_name.lower()

                        key = f"noises.{module_name}.{func_name}"
                        param_classes[key] = param_class

        # Process papers - these don't use parameter classes, just functions
        # We'll add them to the return for consistency but handle them differently
        try:
            papers_modules = papers.__all__
            for module_name in papers_modules:
                # Import the module directly
                module = __import__(f"stimupy.papers.{module_name}", fromlist=[module_name])
                # Get all functions from the module that return stimuli
                if hasattr(module, "__all__"):
                    for func_name in module.__all__:
                        key = f"papers.{module_name}.{func_name}"
                        param_classes[key] = None  # No parameter class for papers
        except (ImportError, AttributeError) as e:
            print(f"Papers module not available: {e}")
            # Continue without papers

    except ImportError as e:
        print(f"Import error: {e}")
        return {}

    return param_classes


def get_stimupy_function(key):
    """Get the corresponding stimupy function for a parameter class key."""
    parts = key.split(".")
    if len(parts) != 3:
        return None

    category, module_name, function_name = parts

    try:
        if category == "components":
            module = getattr(stimupy.components, module_name)
        elif category == "noises":
            module = getattr(stimupy.noises, module_name)
        elif category == "stimuli":
            module = getattr(stimupy.stimuli, module_name)
        elif category == "papers":
            module = __import__(f"stimupy.papers.{module_name}", fromlist=[module_name])
        else:
            return None

        if hasattr(module, function_name):
            return getattr(module, function_name)

        return None

    except AttributeError:
        return None


def generate_and_save_stimulus(key, param_class, output_dir):
    """Generate a stimulus and save it as PNG."""
    try:
        # Get the stimupy function
        func = get_stimupy_function(key)
        if func is None:
            print(f"Could not find stimupy function for {key}")
            return False

        # Handle papers functions (no parameter class) vs regular functions
        if param_class is None:
            # For papers functions, call without arguments
            print(f"Generating {key}...")
            stimulus = func()
        else:
            # Create parameter instance with defaults
            params = param_class()
            stimulus_params = params.get_stimulus_params()

            # Generate the stimulus
            print(f"Generating {key}...")
            stimulus = func(**stimulus_params)

        # Extract the image
        if isinstance(stimulus, dict) and "img" in stimulus:
            img = stimulus["img"]
        elif isinstance(stimulus, np.ndarray):
            img = stimulus
        else:
            print(f"Unexpected stimulus format for {key}: {type(stimulus)}")
            return False

        # Create output filename using the original key with dots
        safe_key = key.replace("/", "_")  # Only replace forward slashes, keep dots
        output_path = output_dir / f"{safe_key}.png"

        # Save the image
        plt.figure(figsize=(8, 8))
        plt.imshow(img, cmap="gray", vmin=0, vmax=1)
        plt.axis("off")
        plt.tight_layout()
        plt.savefig(output_path, dpi=150, bbox_inches="tight", pad_inches=0.1)
        plt.close()

        print(f"Saved: {output_path}")
        return True

    except Exception as e:
        print(f"Error generating {key}: {str(e)}")
        import traceback

        traceback.print_exc()
        return False


def main():
    """Main function to generate all stimulus images."""
    # Create output directory
    output_dir = Path(__file__).parents[2] / "docs" / "_static" / "generated_stimuli"
    output_dir.mkdir(exist_ok=True, parents=True)

    print(f"Output directory: {output_dir}")

    # Discover all parameter classes
    print("Discovering parameter classes...")
    param_classes = get_all_param_classes()
    print(f"Found {len(param_classes)} parameter classes")

    if not param_classes:
        print("No parameter classes found. Check the params module import.")
        return

    # Show discovered classes
    print("\nDiscovered parameter classes:")
    for key in sorted(param_classes.keys()):
        print(f"  {key}")

    # Generate stimuli
    print("\nGenerating stimuli...")
    successful = 0
    failed = 0

    for key, param_class in param_classes.items():
        if generate_and_save_stimulus(key, param_class, output_dir):
            successful += 1
        else:
            failed += 1

    print(f"\nCompleted: {successful} successful, {failed} failed")
    print(f"Images saved to: {output_dir}")


if __name__ == "__main__":
    main()
