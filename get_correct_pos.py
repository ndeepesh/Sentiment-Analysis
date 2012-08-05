def matching_pos(pos):
  if (pos == 'NN'):
    new_pos='n'
  elif (pos == 'JJ'):
    new_pos='a'
  elif (pos == 'RB'):
    new_pos='r'
  elif (pos.startswith('V')):
    new_pos='v'
  else:
    new_pos=""
    
  return new_pos   