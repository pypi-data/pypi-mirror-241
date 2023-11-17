from __future__ import annotations

from typing import Any, Callable, List, Literal

from gradio.components.base import FormComponent
from gradio.events import Events
from gradio.data_classes import FileData, GradioModel

class TextWithAttachmentsData(GradioModel):
    text: str
    attachments: List[FileData]


class TextWithAttachments(FormComponent):
    """
    Creates a very simple textbox for user to enter string input or display string output.
    Preprocessing: passes textbox value as a {str} into the function.
    Postprocessing: expects a {str} returned from function and sets textbox value to it.
    Examples-format: a {str} representing the textbox input.
    """

    EVENTS = [
        "text_change",
        "text_submit",
        "file_upload",
    ]

    data_model = TextWithAttachmentsData

    def __init__(
        self,
        value: TextWithAttachments | Callable | None = None,
        *,
        file_count: Literal["single", "multiple"] = "single",
        button_label: str | None = "📁",
        placeholder: str | None = None,
        label: str | None = None,
        every: float | None = None,
        show_label: bool | None = None,
        scale: int | None = None,
        min_width: int = 160,
        interactive: bool | None = None,
        visible: bool = True,
        rtl: bool = False,
        elem_id: str | None = None,
        elem_classes: list[str] | str | None = None,
        render: bool = True,
        root_url: str | None = None,
        _skip_init_processing: bool = False,
    ):
        """
        Parameters:
            value: default text to provide in textbox. If callable, the function will be called whenever the app loads to set the initial value of the component.
            placeholder: placeholder hint to provide behind textbox.
            label: component name in interface.
            every: If `value` is a callable, run the function 'every' number of seconds while the client connection is open. Has no effect otherwise. Queue must be enabled. The event can be accessed (e.g. to cancel it) via this component's .load_event attribute.
            show_label: if True, will display label.
            scale: relative width compared to adjacent Components in a Row. For example, if Component A has scale=2, and Component B has scale=1, A will be twice as wide as B. Should be an integer.
            min_width: minimum pixel width, will wrap if not sufficient screen space to satisfy this value. If a certain scale value results in this Component being narrower than min_width, the min_width parameter will be respected first.
            interactive: if True, will be rendered as an editable textbox; if False, editing will be disabled. If not provided, this is inferred based on whether the component is used as an input or output.
            visible: If False, component will be hidden.
            rtl: If True and `type` is "text", sets the direction of the text to right-to-left (cursor appears on the left of the text). Default is False, which renders cursor on the right.
            elem_id: An optional string that is assigned as the id of this component in the HTML DOM. Can be used for targeting CSS styles.
            elem_classes: An optional list of strings that are assigned as the classes of this component in the HTML DOM. Can be used for targeting CSS styles.
            render: If False, component will not render be rendered in the Blocks context. Should be used if the intention is to assign event listeners now but render the component later.
            root_url: The remote URL that of the Gradio app that this component belongs to. Used in `gr.load()`. Should not be set manually.
        """
        self.placeholder = placeholder
        self.rtl = rtl
        self.file_count = file_count
        self.button_label = button_label
        super().__init__(
            label=label,
            every=every,
            show_label=show_label,
            scale=scale,
            min_width=min_width,
            interactive=interactive,
            visible=visible,
            elem_id=elem_id,
            elem_classes=elem_classes,
            value=value,
            render=render,
            root_url=root_url,
            _skip_init_processing=_skip_init_processing,
        )

    def preprocess(self, x: TextWithAttachmentsData | dict | None) -> TextWithAttachmentsData | None:
        """
        Preprocesses input (converts it to a string) before passing it to the function.
        Parameters:
            x: text
        Returns:
            TextWithAttachmentsData
        """
        if x is None:
            return None
        return x if isinstance(x, TextWithAttachmentsData) else TextWithAttachmentsData(**x)

    def postprocess(self, y: str | None) -> str | None:
        """
        Postproccess the function output y by converting it to a str before passing it to the frontend.
        Parameters:
            y: function output to postprocess.
        Returns:
            text
        """
        return y

    def example_inputs(self) -> Any:
        return {
            "text": "Look at my dog!",
            "attachments": ["https://gradio-builds.s3.amazonaws.com/diffusion_image/cute_dog.jpg"]
        }
