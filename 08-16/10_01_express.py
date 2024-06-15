from rich.console import Console
from rich.table import Table
from rich.panel import Panel

console = Console()


class Express(dict):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    def get(self, key):
        return super().get(key)

    def setdefault(self, key, value=None):
        if key in self:
            console.print(f"快递公司 [bold cyan]{key}[/bold cyan] 已存在,电话为 [yellow]{self[key]}[/yellow]")
        else:
            super().setdefault(key, value)
            console.print(f"已添加快递公司 [bold cyan]{key}[/bold cyan],电话为 [yellow]{value}[/yellow]")

    def update(self, key, value):
        if key in self:
            super().update({key: value})
            console.print(f"已更新快递公司 [bold cyan]{key}[/bold cyan] 的电话为 [yellow]{value}[/yellow]")
        else:
            console.print(f"快递公司 [bold cyan]{key}[/bold cyan] 不存在,无法更新")

    def pop(self, key):
        value = super().pop(key, None)
        if value:
            console.print(f"已删除快递公司 [bold cyan]{key}[/bold cyan],电话为 [yellow]{value}[/yellow]")
        else:
            console.print(f"快递公司 [bold cyan]{key}[/bold cyan] 不存在,无法删除")

    def traversal(self):
        if not self:
            console.print("[red]当前没有快递公司信息[/red]")
        else:
            table = Table(title="快递公司信息")
            table.add_column("快递公司名称", justify="center", style="cyan")
            table.add_column("电话", justify="center", style="magenta")
            for key, value in self.items():
                table.add_row(key, str(value))
            console.print(table)


express_data = {
    "SF": 95338,
    "ST": 95543,
    "YD": 95546,
    "YTO": 95554,
    "ZTO": 95311,
    "TT": 4001888888,
    "JD": 950616,
    "BS": 95320,
}
e = Express(**express_data)


def multi_input_function(args):
    prompts, func = args
    if prompts:
        return func(*(console.input(p) for p in prompts))
    else:
        return func()


argsmap = {
    "1": (("输入快递公司名称：",), lambda x: console.print(e.get(x) or f"没有找到快递公司：{x}")),
    "2": (("新增加的快递公司名称：", "快递公司电话："), e.setdefault),
    "3": (("要修改的快递公司名称：", "快递公司电话："), e.update),
    "4": (("要删除的快递公司名称：",), e.pop),
    "5": (None, e.traversal)
}


def main():
    while True:
        panel = Panel(
            "1--快递公司查询\n"
            "2--快递公司增加\n"
            "3--快递公司修改\n"
            "4--快递公司删除\n"
            "5--快递公司遍历\n"
            "0--退出",
            title="快递公司管理系统",
            expand=False,
            border_style="bold green"
        )
        console.print(panel)
        inpt = console.input("[bold yellow]请输入选项：[/bold yellow]")

        if inpt == "0":
            break
        elif inpt not in argsmap:
            console.print("[red]输入错误[/red]")
            continue

        multi_input_function(argsmap[inpt])


if __name__ == "__main__":
    main()
    