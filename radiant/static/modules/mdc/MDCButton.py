"""
Brython MDCComponent: MDCButton
===============================
"""
from .core import MDCTemplate


########################################################################
class MDCButton(MDCTemplate):
    """"""

    NAME = 'button', 'MDCButton'

    CSS_classes = {

        'raised': 'mdc-button--raised',
        'unelevated': 'mdc-button--unelevated',
        'outlined': 'mdc-button--outlined',
        'dense': 'mdc-button--dense',

    }

    MDC_optionals = {

        'disabled': 'disabled',
        # 'reversed': 'style = "margin-left: 8px; margin-right: -4px;"',

        # Icons
        'icon': '<i class="material-icons mdc-button__icon" aria-hidden="true">{icon}</i>',
        'fa_icon': '<i class="mdc-button__icon {fa_style} {fa_icon}"></i>',


        'label': '<span class="mdc-button__label">{label}</span>',
        # <i class="material-icons mdc-button__icon" aria-hidden="true">favorite</i>


        # # Icon for icon only
        # 'icon_': '<button class="mdc-icon-button material-icons">{icon_}</button>',
        # 'fa_icon_': '<button class="mdc-icon-button {fa_style} {fa_icon}"></button>',

        # # Icons for a
        # 'icon_a': '<a class="mdc-icon-button material-icons">{icon_}</a>',
        # 'fa_icon_a': '<a class="mdc-icon-button {fa_style} {fa_icon}"></a>',


    }

    # ----------------------------------------------------------------------
    def __new__(self, label=None, href=None, icon=False, style_icon={}, **kwargs):
        """"""
        kwargs.update(self.format_icon(icon))
        del icon

        if kwargs.get('raised', False) or kwargs.get('outlined', False):
            kwargs['unelevated'] = False

        self.element = self.render(locals(), kwargs)

        try:
            self.element.select_one('i').style = style_icon
        except:
            pass

        return self.element

    # ----------------------------------------------------------------------
    @classmethod
    def __html__(cls, **context):
        """"""
        if context.get('href'):
            # if context.get('text'):
            if not context.get('reversed'):
                code = """
                    <a href="{href}" class="mdc-button {CSS_classes}" {disabled}>
                    <div class="mdc-button__ripple"></div>
                    {icon}
                    {fa_icon}
                    {label}
                    </a>
                """
            else:
                code = """
                    <a href="{href}" class="mdc-button {CSS_classes}" {disabled}>
                    <div class="mdc-button__ripple"></div>
                    {label}
                    {icon}
                    {fa_icon}
                    </a>
                """
            # else:
                # code = """
                # {icon_a}
                # {fa_icon_a}
                # """

        else:
            # if context.get('text'):
            if not context.get('reversed'):
                code = """
                    <button class="mdc-button {CSS_classes}" {disabled}>
                    <div class="mdc-button__ripple"></div>
                    {icon}
                    {fa_icon}
                    {label}
                    </button>
                """
            else:
                code = """
                    <button class="mdc-button {CSS_classes}" {disabled}>
                    <div class="mdc-button__ripple"></div>
                    {label}
                    {icon}
                    {fa_icon}
                    </button>

                """
            # else:
                # code = """
                    # {icon_}
                    # {fa_icon_}
                    # """

        return cls.render_html(code, context)


########################################################################
class MDCFab(MDCButton):
    """"""

    CSS_classes = {

        'mini': 'mdc-fab--mini',
        'exited': 'mdc-fab--exited',
        'extended': 'mdc-fab--extended',

    }

    MDC_optionals = {

        'label': '<span class="mdc-fab__label">{label}</span>',
        'disabled': 'disabled',


        'icon': '<i class="material-icons mdc-fab__icon" aria-hidden="true">{icon}</i>',
        'fa_icon': '<i class="mdc-fab__icon {fa_style} {fa_icon}"></i>',

        # 'icon': '<i class="material-icons mdc-button__icon" {reversed} aria-hidden="true">{icon}</i>',
        'fa_icon': '<i class="mdc-button__icon {fa_style} {fa_icon}"></i>',


    }

    # ----------------------------------------------------------------------
    def __new__(self, icon, label=False, **kwargs):
        """"""
        kwargs.update(self.format_icon(icon))
        del icon

        if label:
            extended = True
        else:
            extended = False

        self.element = self.render(locals(), kwargs)
        return self.element

    # ----------------------------------------------------------------------
    @classmethod
    def __html__(cls, **context):
        """"""
        if context.get('href'):

            if not context.get('reversed'):
                code = """
                    <a class="mdc-fab {CSS_classes}" href="{href}" {disabled}>
                      <div class="mdc-fab__ripple"></div>
                      {icon}
                      {fa_icon}
                      {label}
                    </a>
                """
            else:
                code = """
                    <a class="mdc-fab {CSS_classes}" href="{href}" {disabled}>
                      <div class="mdc-fab__ripple"></div>
                      {label}
                      {icon}
                      {fa_icon}
                    </a>
                """

        else:

            if not context.get('reversed'):
                code = """
                    <button class="mdc-fab {CSS_classes}" {disabled}>
                      <div class="mdc-fab__ripple"></div>
                      {icon}
                      {fa_icon}
                      {label}
                    </button>
                """
            else:
                code = """
                    <button class="mdc-fab {CSS_classes}" {disabled}>
                      <div class="mdc-fab__ripple"></div>
                      {label}
                      {icon}
                      {fa_icon}
                    </button>
                """

        return cls.render_html(code, context)


########################################################################
class MDCIconToggle(MDCTemplate):
    """"""

    NAME = 'iconButton', 'MDCIconButtonToggle'

    # ----------------------------------------------------------------------
    def __new__(self, icon_on, icon_off, state='off', **kwargs):
        """"""
        if state == 'on':
            icon_on, icon_off = icon_off, icon_on
        elif state == 'off':
            state = icon_off

        self.element = self.render(locals(), kwargs)
        return self.element

    # ----------------------------------------------------------------------
    @classmethod
    def __html__(cls, **context):
        """"""
        code = """

            <button class="mdc-icon-button" aria-pressed="false">
               <i class="material-icons mdc-icon-button__icon mdc-icon-button__icon--on">{icon_on}</i>
               <i class="material-icons mdc-icon-button__icon">{icon_off}</i>
            </button>

        """

        return cls.render_html(code, context)
