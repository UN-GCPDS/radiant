"""
Brython MDCComponent: MDCLayoutGrid
===================================


"""

from .core import MDCTemplate
#from .MDCButton import MDCButton,  MDCIconToggle


########################################################################
class __cell__(MDCTemplate):
    """"""

    NAME = None, None

    MDC_optionals = {

        'desktop': 'mdc-layout-grid__cell--span-{desktop}-desktop',
        'tablet': 'mdc-layout-grid__cell--span-{tablet}-tablet',
        'mobile': 'mdc-layout-grid__cell--span-{mobile}-mobile',
        'C': 'mdc-layout-grid__cell--span-{C}',

        'index': 'mdc-layout-grid__cell--order-{index}',
        'position': 'mdc-layout-grid__cell--align-{position}',

        'fixed_column_width': 'mdc-layout-grid--fixed-column-width',


    }

    # ----------------------------------------------------------------------

    @classmethod
    def __html__(cls, **context):
        """"""
        code = """
            <div class="mdc-layout-grid__cell {C} {desktop} {tablet} {mobile} {index} {position} {fixed_column_width}"></div>
        """
        return cls.render_html(code, context)


########################################################################
class __grid__(MDCTemplate):
    """"""
    NAME = None, None

    MDC_optionals = {

        'position': 'mdc-layout-grid--align-{position}',

    }

    # ----------------------------------------------------------------------
    @classmethod
    def __html__(cls, **context):
        """"""
        code = """
            <div class="mdc-layout-grid__inner {position}">
            </div>
        """
        return cls.render_html(code, context)

    # ----------------------------------------------------------------------

    @classmethod
    def cell(cls, element, **kwargs):
        """"""
        cell = __cell__(**kwargs)
        cls.element <= cell
        return cell


########################################################################
class MDCLayoutGrid(MDCTemplate):
    """"""

    NAME = None, None

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
    def __new__(self, **kwargs):
        """"""
        # print('QQQQQ')
        self.element = self.render(locals(), kwargs)
        return self.element

    # ----------------------------------------------------------------------

    @classmethod
    def __html__(cls, **context):
        """"""
        code = """
            <div class="mdc-layout-grid">

            </div>
        """

        return cls.render_html(code, context)

    # ----------------------------------------------------------------------

    @classmethod
    def get(self, name):
        """"""
        # if name is 'actions':
            # return self.element.select('.mdc-card__actions')[0]

        # elif name is 'action_buttons':
            # return self.element.select('.mdc-card__action-buttons')[0]

        # elif name is 'action_icons':
            # return self.element.select('.mdc-card__action-icons')[0]

    # ----------------------------------------------------------------------
    @classmethod
    def grid(cls, element, *args, **kwargs):
        """"""
        # print('WWWWWW')
        grid = __grid__(*args, **kwargs)
        cls.element <= grid
        return grid

    # ----------------------------------------------------------------------
    # @classmethod
    # def title(self, mdc, text):
        # """"""
        #self['title'].text = text


