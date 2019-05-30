import openpyxl

wb = openpyxl.Workbook()

sheet = wb.active

sheet.title = 'new title'

sheet['A1'] = '歌曲名'
sheet['B1'] ='所属专辑'
sheet['C1'] ='播放时长'
sheet['D1'] ='播放链接'
rows = [['美国队长','钢铁侠','蜘蛛侠'],['是','漫威','宇宙', '经典','人物']]

for row in rows:
    sheet.append(row)

wb.save('Marvel.xlsx')