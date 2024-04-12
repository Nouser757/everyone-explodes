#works unless 3+3 ants collide simultaneously, gotta rewrite whole collision code probably

from ktools import Edge
import pygame

arrows = [
  ((50, 75), (25, 75), (25, 37.5), (0, 37.5), (37.5, 0), (75, 37.5), (50, 37.5)),
  ((0, 25), (0, 50), (37.5, 50), (37.5, 75), (75, 37.5), (37.5, 0), (37.5, 25)),
  ((25, 0), (50, 0), (50, 37.5), (75, 37.5), (37.5, 75), (0, 37.5), (25, 37.5)),
  ((75, 50), (75, 25), (37.5, 25), (37.5, 0), (0, 37.5), (37.5, 75), (37.5, 50))]

def gameOfAnts(edge: Edge):
  lifegrid = [ #dead, alive
    [0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0]]
  
  antgrid = [ #none, up, right, down, left
    [0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0]]

  def updateInput(screen):
    for i in range(25): pygame.draw.rect(screen, (0,0,0) if lifegrid[i//5][i%5] == 0 else (255,255,255), pygame.Rect((45+(115*(i%5)), 45+(115*(i//5)), 100, 100)))
    for i in range(25): 
      if antgrid[i//5][i%5] != 0: pygame.draw.polygon(screen, (255, 0, 0), [(x+57.5+(115*(i%5)), y+57.5+(115*(i//5))) for x,y in arrows[antgrid[i//5][i%5]-1]])
    pygame.display.flip()

  pygame.init()
  screen = pygame.display.set_mode((650, 650))
  pygame.display.set_caption('Game of Ants - Setup')
  screen.fill((127,127,127))

  updateInput(screen)

  print("Leftclick to toggle cells.")
  print('Rightclick to cycle ants.')

  areas = [pygame.Rect(45+(115*(i%5)), 45+(115*(i//5)), 100, 100) for i in range(25)]
  wait = True
  while wait:
    for event in pygame.event.get():
      if event.type == pygame.QUIT: wait=False
      if event.type == pygame.MOUSEBUTTONUP:
        for i, area in enumerate(areas):
          if area.collidepoint(event.pos):
            if event.button == 1:
              lifegrid[i//5][i%5] = 1-lifegrid[i//5][i%5]
              updateInput(screen)
            elif event.button == 3:
              antgrid[i//5][i%5] = (antgrid[i//5][i%5] + 1)%5
              updateInput(screen)
  pygame.quit()

  def life(lifegrid):
    newgrid = [ #dead, alive
    [0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0]]

    for i, row in enumerate(lifegrid):
      for j, cell in enumerate(row):
        neighbours = [[i-1, j-1], [i-1, j], [i-1, j+1], [i, j-1], [i, j+1], [i+1, j-1], [i+1, j], [i+1, j+1]]
        livecount = 0
        for pair in neighbours:
          if pair[0] < 0 or pair[0] > 4 or pair[1] < 0 or pair[1] > 4:  continue #outside = dead
          else: livecount = livecount + lifegrid[pair[0]][pair[1]]
        
        if cell == 0 and livecount == 3: newgrid[i][j] = 1 #dead, 3 neighbours = alive
        elif cell == 0: continue #dead, <3 or >3 neighbours = dead

        elif cell == 1 and livecount in [2, 3]: newgrid[i][j] = 1 #alive, 2 or 3 neighbours = alive
        else: continue #alive, <2 or >3 neighbours = dead
    
    return newgrid
  
  def ant(lifegrid, antgrid):
    newlife = lifegrid #dead, alive
    newant = [ #none, up, right, down, left
    [0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0]]

    escaped = []

    def move(loc, ant, exit):
      tomove = []
      dirs = [[-1, 0], [0, 1], [1, 0], [0, -1]]
      direction = dirs[ant-1]
      target = [loc[0]+direction[0], loc[1]+direction[1]]

      while True:
        print(target)
        print(tomove)
        if target[0] < 0 or target[0] > 4 or target[1] < 0 or target[1] > 4:
          exit = True
          escaped.append(target)
          break
        elif newant[target[0]][target[1]] == ant:
          target = [target[0]+direction[0], target[1]+direction[1]]
          continue
        elif newant[target[0]][target[1]] > 0:
          tomove.append(target)
          target = [target[0]+direction[0], target[1]+direction[1]]
          continue
        else:
          newant[target[0]][target[1]] = ant
          break
      
      for loc in tomove:
        moving = newant[loc[0]][loc[1]]
        newant[loc[0]][loc[1]] = 0
        exit = move(loc, moving, exit)

      return exit

    exit = False
    for i, row in enumerate(antgrid):
      for j, cell in enumerate(row):
        if cell > 0:
          newlife[i][j] = 1-newlife[i][j]
          exit = move([i, j], cell, exit)

    for i, row in enumerate(newant):
      if exit: break
      for j, cell in enumerate(row):
        if cell > 0:
          screwmath = [4, 1, 2, 3, 4, 1] #maths too hard so i'm just using indexing to make it loop
          newant[i][j] = screwmath[cell + (1 if newlife[i][j] == 1 else -1)]

    return newlife, newant, exit, escaped



  lifegrid = life(lifegrid)

  exit = False
  while not exit: lifegrid, antgrid, exit, escaped = ant(lifegrid, antgrid)

  lifegrid = life(lifegrid)

  pygame.init()
  screen = pygame.display.set_mode((650, 650))
  pygame.display.set_caption('Game of Ants - Output')
  screen.fill((127,127,127))

  for i in range(25): pygame.draw.rect(screen, (0,0,0) if lifegrid[i//5][i%5] == 0 else (255,255,255), pygame.Rect((45+(115*(i%5)), 45+(115*(i//5)), 100, 100)))
  for i in range(25): 
    if antgrid[i//5][i%5] != 0: pygame.draw.polygon(screen, (255, 0, 0), [(x+57.5+(115*(i%5)), y+57.5+(115*(i//5))) for x,y in arrows[antgrid[i//5][i%5]-1]])
  for exit in escaped:
    if exit[0] == -1:
      x = 45+(115*(exit[1]%5))
      y = 0
      w = 100
      h = 45
    elif exit[0] == 5:
      x = 45+(115*(exit[1]%5))
      y = 605
      w = 100
      h = 45
    if exit[1] == -1:
      x = 0
      y = 45+(115*(exit[0]%5))
      w = 45
      h = 100
    if exit[1] == 5:
      x = 605
      y = 45+(115*(exit[0]%5))
      w = 45
      h = 100
    pygame.draw.rect(screen, (255,0,0), pygame.Rect(x, y, w, h))
  
  pygame.display.flip()

  wait = True
  while wait:
    for event in pygame.event.get():
      if event.type == pygame.QUIT: wait=False
  pygame.quit()
