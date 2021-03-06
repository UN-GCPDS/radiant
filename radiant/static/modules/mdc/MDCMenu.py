"""
Brython MDCComponent: MDCMenu
=============================


"""


from browser import window
from .core import MDCTemplate
# from .MDCButton import MDCButton,  MDCIconToggle


########################################################################
class __menuItem__(MDCTemplate):
    """"""

    MDC_optionals = {

        # 'disable': 'tabindex="-1" aria-disabled="true"',
        # 'stack' = '{}'
        'icon': '<i class="radiant-menu-icon material-icons" aria-hidden="true" style="margin-right: 15px;">{icon}</i>',
        'fa_icon': '<i class="radiant-menu-icon {fa_style} {fa_icon}" style="margin-right: 15px;"></i>',

    }

    # ----------------------------------------------------------------------
    def __new__(self, text, icon=None, stack_icon='', disable=False, **kwargs):
        """"""

        if icon and icon.startswith('fa'):
            fa_style = icon[:icon.find('-')]
            fa_icon = 'fa' + icon[icon.find('-'):]
            fa_icon_ = fa_icon
            del icon

        self.element = self.render(locals(), kwargs)

        return self.element

    # ----------------------------------------------------------------------
    @classmethod
    def __html__(cls, **context):
        """"""

        if not context['disable']:
            cls.MDC_optionals['disable'] = 'tabindex="0"'
        else:
            cls.MDC_optionals['disable'] = 'tabindex="-1" aria-disabled="true"',

        code = """
            <li class="mdc-list-item" role="menuitem" {disable}>
                {stack_icon}
                {icon}
                {fa_icon}
                <span class="mdc-list-item__text">{text}</span>
            </li>

        """
        return cls.render_html(code, context)

    # # ----------------------------------------------------------------------
    # @classmethod
    # def get(self, name):
        # """"""
        # if name is 'icon':
            # return self.element.select('.radiant-menu-icon')[0]


########################################################################
class MDCMenu(MDCTemplate):
    """"""

    NAME = 'menu', 'MDCMenu'
    # NAME = 'menuSurface', 'MDCMenuSurface'

    CSS_classes = {

        # '_16_9': 'mdc-card__media--16-9',
        # 'square': 'mdc-card__media--square',
    }

    MDC_optionals = {

        # 'outlined': 'mdc-card--outlined',
        # 'full_bleed': 'mdc-card__actions--full-bleed',
        # 'icon': '<i class="material-icons mdc-button__icon" aria-hidden="true">{icon}</i>',
        # 'disabled': 'disabled',

    }

    # ----------------------------------------------------------------------
    def __new__(self, autoclose=True, **kwargs):
        """"""

        self.element = self.render(locals(), kwargs)

        # if corner in ['BOTTOM_START', 'BOTTOM_LEFT', 'BOTTOM_RIGHT', 'BOTTOM_END', 'TOP_START', 'TOP_LEFT', 'TOP_RIGHT', 'TOP_END']:
            # c = getattr(window.mdc.menu.MDCMenuFoundation.Corner, corner)
            # print(c, self.mdc.setAnchorCorner)
        # self.mdc.setAnchorCorner(window.mdc.menu.MDCMenuFoundation.Corner.BOTTOM_END)

        if autoclose:
            self.element.bind('click', self.toggle)

        return self.element


# menu.setAnchorCorner(mdc.menu.MDCMenuFoundation.Corner.TOP_START)

    # ----------------------------------------------------------------------


    @classmethod
    def __html__(cls, **context):
        """"""

        code = """

        <div class="mdc-menu mdc-menu-surface" tabindex="-1">
          <ul class="mdc-list" role="menu" aria-hidden="true" aria-orientation="vertical">
          </ul>
        </div>

        """
        return cls.render_html(code, context)

    # ----------------------------------------------------------------------

    @classmethod
    def get(self, name):
        """"""
        if name is 'content':
            return self.element.select('.mdc-list')[0]

        # elif name is 'action_buttons':
            # return self.element.select('.mdc-card__action-buttons')[0]

        # elif name is 'action_icons':
            # return self.element.select('.mdc-card__action-icons')[0]

    # ----------------------------------------------------------------------

    @classmethod
    def add_item(cls, element, *args, **kwargs):
        """"""
        item = __menuItem__(*args, **kwargs)
        cls.get('content') <= item
        return item

    # ----------------------------------------------------------------------

    @classmethod
    def add_divider(cls, element):
        """"""
        divider = '<li class="mdc-list-divider" role="separator"></li>'
        divider = cls.render_str(divider)
        cls.get('content') <= divider

    # ----------------------------------------------------------------------
    @classmethod
    def toggle(cls, element, *args, **kwargs):
        """"""
        # if corner in ['BOTTOM_START', 'BOTTOM_LEFT', 'BOTTOM_RIGHT', 'BOTTOM_END', 'TOP_START', 'TOP_LEFT', 'TOP_RIGHT', 'TOP_END']:
            # c = getattr(window.mdc.menuSurface.Corner, corner)
            # cls.mdc.setAnchorCorner(c)

        cls.mdc.open = not cls.mdc.open
        # self['title'].text = text


