def get_info_list(tr):
    info_list = []
    th_tds = None
    for cell in tr:
      if cell.name=='th':
        if not th_tds:
          th_tds = [cell]
        else:
          info_list.append(th_tds)
          th_tds=None
      else:
        if not th_tds:
          th_tds = [cell]
        else:
          th_tds.append(cell)
    if th_tds:
      info_list.append(th_tds)

    return info_list
