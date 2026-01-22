#!/usr/bin/env python3
"""
庆祝星星 GIF - 星星从天而降，弹跳，带脉冲和闪光效果
优化用于 Slack emoji
"""

import sys
import math
sys.path.insert(0, '/Users/owen/.claude/skills/slack-gif-creator')

from PIL import Image, ImageDraw
from core.gif_builder import GIFBuilder
from core.easing import interpolate
from core.frame_composer import create_gradient_background

# 参数
WIDTH = 128
HEIGHT = 128
FPS = 15
DURATION = 2.0  # 秒
NUM_FRAMES = int(FPS * DURATION)

# 创建 GIF 构建器
builder = GIFBuilder(width=WIDTH, height=HEIGHT, fps=FPS)

def draw_star_custom(draw, cx, cy, outer_radius, inner_radius, fill, outline=None, outline_width=1, rotation=0):
    """绘制5角星"""
    points = []
    for i in range(10):
        angle = (i * 36 - 90 + rotation) * math.pi / 180
        radius = outer_radius if i % 2 == 0 else inner_radius
        px = cx + radius * math.cos(angle)
        py = cy + radius * math.sin(angle)
        points.append((px, py))
    
    draw.polygon(points, fill=fill, outline=outline, width=outline_width)

# 动画阶段
FALL_FRAMES = 15  # 下落阶段
BOUNCE_FRAMES = 10  # 弹跳阶段
PULSE_FRAMES = NUM_FRAMES - FALL_FRAMES - BOUNCE_FRAMES  # 脉冲阶段

for frame_idx in range(NUM_FRAMES):
    # 创建渐变背景（深蓝到浅蓝）
    frame = create_gradient_background(
        WIDTH, HEIGHT,
        top_color=(25, 35, 60),
        bottom_color=(40, 60, 100)
    )
    draw = ImageDraw.Draw(frame)
    
    # 计算星星的位置和大小
    center_x = WIDTH // 2
    
    if frame_idx < FALL_FRAMES:
        # 阶段 1: 从顶部下落
        t = frame_idx / FALL_FRAMES
        y = interpolate(-30, HEIGHT - 40, t, easing='ease_in')
        size = 25
        rotation = t * 360 * 2  # 旋转两圈
        
    elif frame_idx < FALL_FRAMES + BOUNCE_FRAMES:
        # 阶段 2: 弹跳
        t = (frame_idx - FALL_FRAMES) / BOUNCE_FRAMES
        base_y = HEIGHT - 40
        bounce_offset = interpolate(0, -15, t, easing='bounce_out')
        y = base_y + bounce_offset
        size = 25
        rotation = 0
        
    else:
        # 阶段 3: 脉冲闪烁
        t = (frame_idx - FALL_FRAMES - BOUNCE_FRAMES) / PULSE_FRAMES
        y = HEIGHT - 40
        # 心跳式脉冲
        pulse = math.sin(t * 8 * math.pi) * 0.15 + 1
        size = int(25 * pulse)
        rotation = math.sin(t * 4 * math.pi) * 5  # 轻微摆动
    
    # 绘制发光效果（多层半透明星星）
    for glow_layer in range(3, 0, -1):
        glow_size = size + glow_layer * 6
        glow_alpha = int(40 / glow_layer)
        
        # 创建半透明层
        glow_frame = Image.new('RGBA', (WIDTH, HEIGHT), (0, 0, 0, 0))
        glow_draw = ImageDraw.Draw(glow_frame)
        
        # 绘制发光星星
        draw_star_custom(
            glow_draw,
            center_x, int(y),
            outer_radius=glow_size,
            inner_radius=int(glow_size * 0.4),
            fill=(255, 220, 100, glow_alpha),
            outline=None,
            rotation=rotation
        )
        
        # 合成到主帧
        frame = Image.alpha_composite(frame.convert('RGBA'), glow_frame)
    
    # 绘制主星星
    star_frame = Image.new('RGBA', (WIDTH, HEIGHT), (0, 0, 0, 0))
    star_draw = ImageDraw.Draw(star_frame)
    
    draw_star_custom(
        star_draw,
        center_x, int(y),
        outer_radius=size,
        inner_radius=int(size * 0.4),
        fill=(255, 235, 59, 255),  # 金黄色
        outline=(255, 193, 7, 255),  # 深金色边框
        outline_width=3,
        rotation=rotation
    )
    
    # 添加高光点
    highlight_size = max(3, int(size * 0.15))
    star_draw.ellipse(
        [center_x - size//3 - highlight_size, int(y) - size//3 - highlight_size,
         center_x - size//3 + highlight_size, int(y) - size//3 + highlight_size],
        fill=(255, 255, 255, 200)
    )
    
    # 合成星星
    frame = Image.alpha_composite(frame.convert('RGBA'), star_frame)
    
    # 添加闪光粒子（在脉冲阶段）
    if frame_idx >= FALL_FRAMES + BOUNCE_FRAMES:
        t = (frame_idx - FALL_FRAMES - BOUNCE_FRAMES) / PULSE_FRAMES
        for i in range(8):
            angle = (i / 8) * 2 * math.pi + t * math.pi
            dist = 40 + math.sin(t * 6 * math.pi + i) * 10
            px = center_x + math.cos(angle) * dist
            py = y + math.sin(angle) * dist
            
            sparkle_size = 2 + int(math.sin(t * 12 * math.pi + i * 0.5) * 2)
            alpha = int(150 + math.sin(t * 12 * math.pi + i) * 100)
         
            sparkle_frame = Image.new('RGBA', (WIDTH, HEIGHT), (0, 0, 0, 0))
            sparkle_draw = ImageDraw.Draw(sparkle_frame)
            sparkle_draw.ellipse(
                [px - sparkle_size, py - sparkle_size,
                 px + sparkle_size, py + sparkle_size],
                fill=(255, 255, 200, alpha)
            )
            frame = Image.alpha_composite(frame, sparkle_frame)
    
    # 转换回 RGB 并添加到构建器
    builder.add_frame(frame.convert('RGB'))
    
    # 显示进度
    if (frame_idx + 1) % 5 == 0:
        print(f"生成帧 {frame_idx + 1}/{NUM_FRAMES}...")

# 保存优化的 GIF
output_path = '/Users/owen/.claude/skills/slack-gif-creator/celebration_star.gif'
print(f"\n正在优化并保存 GIF...")
builder.save(
    output_path,
    num_colors=64,
    optimize_for_emoji=True,
    remove_duplicates=True
)

print(f"\n✨ GIF 创建成功!")
print(f"📁 保存位置: {output_path}")
print(f"📊 帧数: {NUM_FRAMES}")
print(f"🎬 FPS: {FPS}")
print(f"⏱️  时长: {DURATION}秒")

# 验证 GIF
print(f"\n正在验证 Slack 兼容性...")
from core.validators import validate_gif
passes, info = validate_gif(output_path, is_emoji=True, verbose=True)
if passes:
    print("✅ GIF 符合 Slack emoji 标准！")
else:
    print("⚠️ GIF 可能需要进一步优化")
