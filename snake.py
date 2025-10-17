import random

width, height = 600, 200
segments = 20
snake_length = 8

# Генерируем случайные сегменты змейки
snake = [(random.randint(0, segments-1), random.randint(0, segments-1)) for _ in range(snake_length)]

# SVG-шаблон
svg_dark = f'<svg width="{width}" height="{height}" xmlns="http://www.w3.org/2000/svg" style="background:#0d1117">'
svg_light = f'<svg width="{width}" height="{height}" xmlns="http://www.w3.org/2000/svg" style="background:#fff">'

for x, y in snake:
    svg_dark += f'<rect x="{x*30}" y="{y*20}" width="28" height="18" fill="lime" />'
    svg_light += f'<rect x="{x*30}" y="{y*20}" width="28" height="18" fill="green" />'

svg_dark += '</svg>'
svg_light += '</svg>'

# Сохраняем
with open('output/github-snake-dark.svg', 'w') as f:
    f.write(svg_dark)

with open('output/github-snake.svg', 'w') as f:
    f.write(svg_light)
