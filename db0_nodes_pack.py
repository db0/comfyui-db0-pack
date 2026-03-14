import re
from comfy_api.latest import ComfyExtension, io
from typing_extensions import override

class RegexMatchToFloat(io.ComfyNode):
    @classmethod
    def define_schema(cls):
        return io.Schema(
            node_id="RegexMatchToFloat",
            display_name="Regex Match To Float",
            category="db0",
            description="If regex matches, returns a float if regex matches",
            inputs=[
                io.String.Input("string", multiline=True),
                io.String.Input("regex_pattern", multiline=True),
                io.Float.Input("output_on_match"),
                io.Float.Input("output_on_non_match"),
                io.Boolean.Input("case_insensitive", default=True, optional=True, advanced=True),
                io.Boolean.Input("multiline", default=False, optional=True, advanced=True),
                io.Boolean.Input("dotall", default=False, optional=True, advanced=True, tooltip="When enabled, the dot (.) character will match any character including newline characters. When disabled, dots won't match newlines."),
            ],
            outputs=[
                io.Float.Output(),
            ]
        )

    @classmethod
    def execute(cls, string, regex_pattern, output_on_match, output_on_non_match, case_insensitive=True, multiline=False, dotall=False):
        flags = 0

        if case_insensitive:
            flags |= re.IGNORECASE
        if multiline:
            flags |= re.MULTILINE
        if dotall:
            flags |= re.DOTALL
        if re.search(regex_pattern, string, flags=flags):
            return io.NodeOutput(output_on_match)
        else:
            return io.NodeOutput(output_on_non_match)


class RegexMatchToString(io.ComfyNode):
    @classmethod
    def define_schema(cls):
        return io.Schema(
            node_id="RegexMatchToString",
            display_name="Regex Match To String",
            category="db0",
            description="If regex matches, returns a string,, else return another string",
            inputs=[
                io.String.Input("string", multiline=True),
                io.String.Input("regex_pattern", multiline=True),
                io.String.Input("output_on_match", multiline=True),
                io.String.Input("output_on_non_match", multiline=True),
                io.Boolean.Input("case_insensitive", default=True, optional=True, advanced=True),
                io.Boolean.Input("multiline", default=False, optional=True, advanced=True),
                io.Boolean.Input("dotall", default=False, optional=True, advanced=True, tooltip="When enabled, the dot (.) character will match any character including newline characters. When disabled, dots won't match newlines."),
            ],
            outputs=[
                io.String.Output(),
            ]
        )

    @classmethod
    def execute(cls, string, regex_pattern, output_on_match, output_on_non_match, case_insensitive=True, multiline=False, dotall=False):
        flags = 0

        if case_insensitive:
            flags |= re.IGNORECASE
        if multiline:
            flags |= re.MULTILINE
        if dotall:
            flags |= re.DOTALL
        if re.search(regex_pattern, string, flags=flags):
            return io.NodeOutput(output_on_match)
        else:
            return io.NodeOutput(output_on_non_match)


class Db0Extension(ComfyExtension):
    @override
    async def get_node_list(self) -> list[type[io.ComfyNode]]:
        return [
            RegexMatchToFloat,
            RegexMatchToString,
        ]

async def comfy_entrypoint() -> Db0Extension:
    return Db0Extension()
