"""Minimal markdown -> HTML for the study-guide files (headings, bullets, nested bullets,
paragraphs, bold, italics, inline code, tables, links). Escapes everything else."""
import html, re

def inline(s):
    s = html.escape(s, quote=False)
    s = re.sub(r'`([^`]+)`', r'<code>\1</code>', s)
    s = re.sub(r'\*\*([^*]+)\*\*', r'<strong>\1</strong>', s)
    s = re.sub(r'(?<![\w*])\*([^*\n]+)\*(?![\w*])', r'<em>\1</em>', s)
    s = re.sub(r'\[([^\]]+)\]\((https?://[^)\s]+)\)', r'<a href="\2" target="_blank" rel="noopener">\1</a>', s)
    # trailing source tags like [MCL 500.3107(1)(b)] -> styled cite
    # bracketed source tags like [MCL 500.3107(1)(b)] or [IRMI "hazard"] -> styled cite (links already converted)
    s = re.sub(r'\[([^\[\]]{2,})\](?!\()', r'<cite>[\1]</cite>', s)
    return s

def convert(md):
    lines = md.split('\n')
    out, stack, para, i = [], [], [], 0
    def close_lists(level=0):
        while len(stack) > level:
            out.append('</li></ul>')
            stack.pop()
    def flush_para():
        if para:
            out.append('<p>' + inline(' '.join(para)) + '</p>')
            para.clear()
    while i < len(lines):
        ln = lines[i].rstrip()
        if not ln.strip():
            flush_para(); i += 1; continue
        m = re.match(r'^(#{1,6})\s+(.*)$', ln)
        if m:
            flush_para(); close_lists()
            lvl = min(len(m.group(1)) + 1, 6)
            out.append(f'<h{lvl}>{inline(m.group(2))}</h{lvl}>')
            i += 1; continue
        if ln.strip().startswith('|') and i + 1 < len(lines) and re.match(r'^\s*\|?\s*:?-{2,}', lines[i+1]):
            flush_para(); close_lists()
            rows = []
            while i < len(lines) and lines[i].strip().startswith('|'):
                rows.append([c.strip() for c in lines[i].strip().strip('|').split('|')])
                i += 1
            head, body = rows[0], [r for r in rows[2:]]
            t = '<div class="tbl"><table><thead><tr>' + ''.join(f'<th>{inline(c)}</th>' for c in head) + '</tr></thead><tbody>'
            for r in body:
                t += '<tr>' + ''.join(f'<td>{inline(c)}</td>' for c in r) + '</tr>'
            out.append(t + '</tbody></table></div>')
            continue
        m = re.match(r'^(\s*)([-*+]|\d+[.)])\s+(.*)$', ln)
        if m:
            flush_para()
            depth = len(m.group(1).replace('\t', '    ')) // 2 + 1
            depth = min(depth, len(stack) + 1)
            if depth > len(stack):
                out.append('<ul>'); stack.append(depth); out.append('<li>')
            else:
                close_lists(depth)
                out.append('</li><li>')
            out.append(inline(m.group(3)))
            i += 1; continue
        if stack and lines[i].startswith(' '):
            out.append(' ' + inline(ln.strip())); i += 1; continue
        close_lists()
        para.append(ln.strip()); i += 1
    flush_para(); close_lists()
    return '\n'.join(out)
