load("http.star", "http")
load("render.star", "render")

def main(config):
    res = http.get("https://y-maedomari-p.github.io/train-app/timetable.txt")
    lines = res.body().split("\n")

    # ラベル付き行を作成（最大3行）
    labeled_lines = []
    icons = ["[1]", "[2]", "[3]"]

    i = 0
    for line in lines:
        if i >= 3:
            break
        labeled_lines.append(icons[i] + " " + line)
        i += 1

    # Textオブジェクトを1つずつ手動で作成
    text_widgets = []
    for line in labeled_lines:
        text_widgets.append(
            render.Text(
                content = line,
                font = "tb-8"
            )
        )

    return render.Root(
        child = render.Column(
            children = text_widgets
        )
    )
