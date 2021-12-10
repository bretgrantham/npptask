import re
import time

def __copyUnfinishedItem(m):
    editor.documentEnd()
    editor.addText(m.group())
    editor.newLine()

def __copyPreviousUnfinishedItems(endPos):
    startPos = editor.positionFromLine(editor.lineFromPosition(editor.searchPrev(FINDOPTION.REGEXP, r'^\* Entry:.+$')) + 1)
    editor.research(r'(?!^\s*$)(?!^.*DONE!.*$)(^.+$)', __copyUnfinishedItem, re.MULTILINE, startPos, max(startPos, endPos))

editor.documentEnd()
editor.searchAnchor()
endPos = editor.getCurrentPos()
editor.research(r'(?!^\s*$)(^.*$)', lambda m: editor.newLine(), 0, editor.positionFromLine(-1))
editor.newLine()
editor.addText('* Entry: ' + time.strftime ('%m/%d/%Y %I:%M %p') + ' ****************************************')
editor.newLine()
editor.newLine()
__copyPreviousUnfinishedItems(endPos)
editor.documentEnd()
