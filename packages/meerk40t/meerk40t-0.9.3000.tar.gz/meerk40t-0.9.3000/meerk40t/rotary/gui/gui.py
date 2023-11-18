ROTARY_VIEW = False


def plugin(kernel, lifecycle):
    if lifecycle == "cli":
        kernel.set_feature("rotary")
    if lifecycle == "invalidate":
        return not kernel.has_feature("wx")
    if lifecycle == "register":
        from meerk40t.gui.icons import icon_rotary
        from meerk40t.rotary.gui.rotarysettings import RotarySettings

        _ = kernel.translation
        # Disable Rotary for the time being as it is not yet fully working...
        enable_rotary = False
        if not enable_rotary:
            return

        kernel.register("window/Rotary", RotarySettings)
        kernel.register(
            "button/device/Rotary",
            {
                "label": _("Rotary"),
                "icon": icon_rotary,
                "tip": _("Opens Rotary Window"),
                "action": lambda v: kernel.console("window toggle Rotary\n"),
            },
        )

        @kernel.console_command("rotaryview", help=_("Rotary View of Scene"))
        def toggle_rotary_view(*args, **kwargs):
            """
            Rotary Stretch/Unstretch of Scene based on values in rotary service
            """
            global ROTARY_VIEW
            rotary = kernel.rotary
            if ROTARY_VIEW:
                rotary(f"scene aspect {rotary.scale_x} {rotary.scale_y}\n")
            else:
                try:
                    rotary(
                        f"scene aspect {1.0 / rotary.scale_x} {1.0 / rotary.scale_y}\n"
                    )
                except ZeroDivisionError:
                    pass
            ROTARY_VIEW = not ROTARY_VIEW
