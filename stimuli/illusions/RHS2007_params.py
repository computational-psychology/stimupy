{
    "WE-thick": {
        "source": ["Blakeslee and McCourt (1999)", "White (1979)"],
        "illusion": "Whites_classic",
        "grating": {
            "wave": "square",
            "orientation": "horizontal",  # direction of wave
            "n_cycles": 4,  # full cycles (white + black)
            "phase": 0,  # starting phase (bar), 0 = black
            "height": 12,  # deg, height of grating
            "phase_width": 2,  # deg, wwidth of single phase (bar)
            "width": 16,  # deg, phase_width * 2 * n_cycles
        },
        "target": [
            {
                "shape": (2, 4),  # deg, width, height
                "phase_idx": 3,  # which phase (bar) target is on
                "offset": 0,  # deg, vertical distance from horizontal meridian
            },
            {
                "shape": (2, 4),  # deg, width, height
                "phase_idx": 5,  # which phase (bar) target is on
                "offset": 0,  # deg, vertical distance from horizontal meridian
            },
        ],
    },
    "WE-thin-wide": {
        "source": ["Blakeslee and McCourt (1999)", "White (1979)"],
        "illusion": "Whites_classic",
        "grating": {
            "wave": "square",
            "orientation": "horizontal",  # direction of wave
            "n_cycles": 8,  # full cycles (white + black)
            "phase": 1,  # starting phase (bar), 0 = black
            "height": 12,  # deg, height of grating
            "phase_width": 1,  # deg, wwidth of single phase (bar)
            "width": 16,  # deg, phase_width * 2 * n_cycles
        },
        "target": [
            {
                "shape": (1, 2),  # deg, width, height
                "phase_idx": 4,  # which phase (bar) target is on
                "offset": 0,  # deg, vertical distance from horizontal meridian
            },
            {
                "shape": (1, 2),  # deg, width, height
                "phase_idx": 13,  # which phase (bar) target is on
                "offset": 0,  # deg, vertical distance from horizontal meridian
            },
        ],
    },
    "WE-dual": {
        "source": "Robinson, Hammon, and De SA (2007)",
        "stimuli": [
            {
                "grating": {
                    "wave": "square",
                    "orientation": "horizontal",  # direction of wave
                    "n_cycles": 4,  # full cycles (white + black)
                    "phase": 0,  # starting phase (left bar), 0 = black
                    "height": 6,  # deg, height of grating
                    "phase_width": 1,  # deg, wwidth of single phase (bar)
                    "width": 8,  # deg, phase_width * 2 * n_cycles
                },
                "target": [
                    {
                        "shape": (1, 2),  # deg, width, height
                        "phase_idx": 3,  # which phase (bar) target is on
                        "offset": 0,  # deg, vertical distance from horizontal meridian
                    },
                    {
                        "shape": (1, 2),  # deg, width, height
                        "phase_idx": 5,  # which phase (bar) target is on
                        "offset": 0,  # deg, vertical distance from horizontal meridian
                    },
                ],
            },
            {
                "grating": {
                    "wave": "square",
                    "orientation": "vertical",  # direction of wave
                    "n_cycles": 4,  # full cycles (white + black)
                    "phase": 0,  # starting phase (top bar), 0 = black
                    "width": 6,  # deg, height of grating
                    "phase_height": 1,  # deg, wwidth of single phase (bar)
                    "height": 8,  # deg, phase_width * 2 * n_cycles
                },
                "target": [
                    {
                        "shape": (2, 1),  # deg, width, height
                        "phase_idx": 3,  # which phase (bar) target is on
                        "offset": 0,  # deg, horizontal distance from grating meridian
                    },
                    {
                        "shape": (2, 1),  # deg, width, height
                        "phase_idx": 5,  # which phase (bar) target is on
                        "offset": 0,  # deg, horizontal distance from grating meridian
                    },
                ],
            },
        ],
    },
    "WE-Anderson": {
        "source": ["Blakeslee et al. (2005)", "Anderson (2001)"],
        "target_shape": [1, 3],
    },
    "WE-Howe": {
        "source": ["Blakeslee et al. (2005)", "Howe (2001)"],
        "target_shape": [1, 3],
    },
    "WE-zigzag": {
        "source": ["Based on Clifford and Spehar (2003)"],
        "target_shape": [1, 3],
    },
    "WE-radial-thick-small": {
        "source": "Based on Anstis (2003)",
        "grating": {
            "wave": "square",
            "orientation": "circular",
            "radius": 8,  # maybe? Looks like twice the height of the target (4deg, according to table)
            "phase": 0,  # black, first segment from right, counterclockwise
            "n_cycles": 7,
            "height": 16,  # deg, 2 * radius
            "width": 16,  # deg, 2 * radius
        },
        "target": [
            {
                "height": 4,  # deg, height
                "phase_idx": 4,  # which phase (segment) target is on
                "offset": 2,  # maybe? deg, from origin
            },
            {
                "height": 4,  # deg, height
                "phase_idx": 11,  # which phase (segment) target is on
                "offset": 2,  # maybe? deg, from origin
            },
        ],
    },
    "WE-radial-thick": {
        "source": "Based on Anstis (2003)",
        "grating": {
            "wave": "square",
            "orientation": "circular",
            "radius": 12,  # maybe?
            "phase": 1,  # white, first segment from right, counterclockwise
            "n_cycles": 9,
            "height": 24,  # deg, 2 * radius
            "width": 24,  # deg, 2 * radius
        },
        "target": [
            {
                "height": 4,  # deg, height
                "phase_idx": 5,  # which phase (segment) target is on
                "offset": 4,  # maybe? deg, from origin
            },
            {
                "height": 4,  # deg, height
                "phase_idx": 14,  # which phase (segment) target is on
                "offset": 4,  # maybe? deg, from origin
            },
        ],
    },
    "WE-radial-thin-small": {
        "source": "Based on Anstis (2003)",
        "grating": {
            "wave": "square",
            "orientation": "circular",
            "radius": 8,  # maybe? Looks like twice the height of the target (4deg, according to table)
            "phase": 1,  # black, first segment from right, counterclockwise
            "n_cycles": 13,
            "height": 16,  # deg, 2 * radius
            "width": 16,  # deg, 2 * radius
        },
        "target": [
            {
                "height": 2,  # deg, height
                "phase_idx": 7,  # which phase (segment) target is on
                "offset": 3,  # maybe? deg, from origin
            },
            {
                "height": 2,  # deg, height
                "phase_idx": 20,  # which phase (segment) target is on
                "offset": 3,  # maybe? deg, from origin
            },
        ],
    },
    "WE-radial-thin": {
        "source": "Based on Anstis (2003)",
        "grating": {
            "wave": "square",
            "orientation": "circular",
            "radius": 12,  # maybe?
            "phase": 1,  # white, first segment from right, counterclockwise
            "n_cycles": 21,
            "height": 24,  # deg, 2 * radius
            "width": 24,  # deg, 2 * radius
        },
        "target": [
            {
                "height": 2,  # deg, height
                "phase_idx": 11,  # which phase (segment) target is on
                "offset": 5,  # maybe? deg, from origin
            },
            {
                "height": 2,  # deg, height
                "phase_idx": 32,  # which phase (segment) target is on
                "offset": 5,  # maybe? deg, from origin
            },
        ],
    },
    "WE-circular1": {
        "source": "Based on Howe (2005)",
        "stimuli": [
            {
                "grating": {
                    "orientation": "radial",
                    "phase": 1,  # white, starting phase (center)
                    "phase_width": 1,  # deg, thickness of phase (ring)
                    "n_cycles": 4,  # full cycles, i.e., black+white rings
                    "radius": 8,  # deg, phase_width*2*n_cycles
                    "width": 16,  # deg 2*radius
                    "height": 16,  # deg 2*radius
                },
                "target": {"phase_idx": 5},
            },
            {
                "grating": {
                    "orientation": "radial",
                    "phase": 0,  # white, starting phase (center)
                    "phase_width": 1,  # deg, thickness of phase (ring)
                    "n_cycles": 4,  # full cycles, i.e., black+white rings
                    "radius": 8,  # deg, phase_width*2*n_cycles
                    "width": 16,  # deg 2*radius
                    "height": 16,  # deg 2*radius
                },
                "target": {"phase_idx": 5},
            },
        ],
    },
    "WE-circular.5": {
        "source": "Based on Howe (2005)",
        "stimuli": [
            {
                "grating": {
                    "orientation": "radial",
                    "phase": 1,  # white, starting phase (center)
                    "phase_width": 0.5,  # deg, thickness of phase (ring)
                    "n_cycles": 8,  # full cycles, i.e., black+white rings
                    "radius": 8,  # deg, phase_width*2*n_cycles
                    "width": 16,  # deg 2*radius
                    "height": 16,  # deg 2*radius
                },
                "target": {"phase_idx": 11},
            },
            {
                "grating": {
                    "orientation": "radial",
                    "phase": 0,  # white, starting phase (center)
                    "phase_width": 0.5,  # deg, thickness of phase (ring)
                    "n_cycles": 8,  # full cycles, i.e., black+white rings
                    "radius": 8,  # deg, phase_width*2*n_cycles
                    "width": 16,  # deg 2*radius
                    "height": 16,  # deg 2*radius
                },
                "target": {"phase_idx": 11},
            },
        ],
    },
    "WE-circular.25": {
        "source": "Based on Howe (2005)",
        "stimuli": [
            {
                "grating": {
                    "orientation": "radial",
                    "phase": 1,  # white, starting phase (center)
                    "phase_width": 0.25,  # deg, thickness of phase (ring)
                    "n_cycles": 16,  # full cycles, i.e., black+white rings
                    "radius": 8,  # deg, phase_width*2*n_cycles
                    "width": 16,  # deg 2*radius
                    "height": 16,  # deg 2*radius
                },
                "target": {"phase_idx": 23},
            },
            {
                "grating": {
                    "orientation": "radial",
                    "phase": 0,  # white, starting phase (center)
                    "phase_width": 0.25,  # deg, thickness of phase (ring)
                    "n_cycles": 16,  # full cycles, i.e., black+white rings
                    "radius": 8,  # deg, phase_width*2*n_cycles
                    "width": 16,  # deg 2*radius
                    "height": 16,  # deg 2*radius
                },
                "target": {"phase_idx": 23},
            },
        ],
    },
    "Grating_induction": {
        "source": ["Blakeslee and McCourt (1999)", "McCourt (1982)"],
        "grating": {
            "wave": "sine",
            "orientation": "horizontal",  # direction of wave
            "n_cycles": 4,  # full cycles (white + black)
            "phase": 1,  # starting phase (bar), 0 = black
            "height": 12,  # deg, height of grating
            "phase_width": 2,  # deg, wwidth of single phase (bar)
            "width": 16,  # deg, phase_width * 2 * n_cycles
        },
        "target": {"height": 1},  # deg, height of neutral bar in center
    },
    "SBC-large": {
        "source": "Blakeslee and McCourt (1999)",
        "illusion": "simultaneous brightness contrast",
        "stimuli": [
            {
                "background": {"height": 12, "width": 15, "phase": 1},
                "target": {"width": 3, "height": 3},  # deg
            },
            {
                "background": {"height": 12, "width": 15, "phase": 0},
                "target": {"width": 3, "height": 3},  # deg
            },
        ],
    },
    "SBC-small": {
        "source": "Blakeslee and McCourt (1999)",
        "illusion": "simultaneous brightness contrast",
        "stimuli": [
            {
                "background": {"height": 12, "width": 15, "phase": 1},
                "target": {"width": 1, "height": 1},  # deg
            },
            {
                "background": {"height": 12, "width": 15, "phase": 0},
                "target": {"width": 1, "height": 1},  # deg
            },
        ],
    },
    "Todorovic-equal": {
        "source": ["Blakeslee and McCourt (1999)", "Pessoa et al. (1998)"],
        "cross_length": 8,
    },
    "Todorovic-in-large": {
        "source": ["Blakeslee and McCourt (1999)", "Todorovic (1997)"],
        "cross_length": 5.3,
    },
    "Todorovic-in-small": {
        "source": ["Blakeslee and McCourt (1999)", "Todorovic (1997)"],
        "cross_length": 3,
    },
    "Todorovic-out": {
        "source": ["Blakeslee and McCourt (1999)", "Pessoa et al. (1998)"],
        "cross_length": 8.7,
    },
    "Checkerboard-0.156": {
        "source": ["Blakeslee and McCourt (2004)", "DeValois and DeValois (1988)"],
        "checkerboard": {
            "check_height": 0.156,  # deg
            "check_width": 0.156,  # deg
            "n_checks": (102, 40),  # number of checks, (width, height)
            "width": 15.91,  # deg
            "height": 6.57,  # deg
        },
        "target": [
            {
                "height": 0.156,  # deg
                "width": 0.156,  # deg
                "phase_idx": 17,  # which check is target on?
            },
            {
                "height": 0.156,  # deg
                "width": 0.156,  # deg
                "phase_idx": 86,  # which check is target on?
            },
        ],
    },
    "Checkerboard-0.938": {
        "source": ["Blakeslee and McCourt (2004)", "DeValois and DeValois (1988)"],
        "checkerboard": {
            "check_height": 0.938,  # deg
            "check_width": 0.938,  # deg
            "n_checks": (25, 7),  # number of checks, (width, height)
            "width": 18.8,  # deg
            "height": 6.57,  # deg
        },
        "target": [
            {"height": 0.938, "width": 0.938, "phase_idx": 7},  # deg  # deg
            {"height": 0.938, "width": 0.938, "phase_idx": 18},  # deg  # deg
        ],
    },
    "Checkerboard-2.09": {
        "source": ["Blakeslee and McCourt (2004)", "DeValois and DeValois (1988)"],
        "checkerboard": {
            "check_height": 2.09,  # deg
            "check_width": 2.09,  # deg
            "n_checks": (10, 3),  # number of checks, (width, height)
            "width": 20.09,  # deg
            "height": 6.27,  # deg
        },
        "target": [
            {
                "height": 2.09,  # deg
                "width": 2.09,  # deg
                "phase_idx": 3,  # which check is target on?
            },
            {
                "height": 2.09,  # deg
                "width": 2.09,  # deg
                "phase_idx": 8,  # which check is target on?
            },
        ],
    },
    "Corrugated Mondrian": {
        "source": ["Blakeslee and McCourt (2001)", "Adelson (1993)"],
        "target_shape": [2, 2],
    },
    "Benary cross": {
        "source": ["Blakeslee and McCourt (2001)", "Benary (1924)"],
        "target_hypothenuse": 3,
    },
    "Todorovic Benary 1–2": {
        "source": ["Blakeslee and McCourt (2001)", "Todorovic (1997)"],
        "target_hypothenuse": 3,
    },
    "Todorovic Benary 3–4": {
        "source": ["Blakeslee and McCourt (2001)", "Todorovic (1997)"],
        "target_hypothenuse": 3,
    },
    "Bullseye-thin": {"source": "Bindman and Chubb (2004)", "width": 0.608},
    "Bullseye-thick": {"source": "Bindman and Chubb (2004)", "width": 0.608},
}
