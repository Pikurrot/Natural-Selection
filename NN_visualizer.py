import pygame
import numpy as np

def visualize(screen,weights,biases,inputs=np.array([]),outputs=np.array([])):
	pygame.font.init()
	gui_x,gui_y = screen.get_size()
	screen.fill((255,255,255))

	n_layers = len(weights)+1
	n_inputs = weights[0].shape[0]
	n_outputs = weights[-1].shape[1]
	n_neurons = [n_inputs]+[len(l) for l in biases]+[n_outputs]

	x_offset = gui_x/20
	y_offset = gui_y/20
	neuron_size = 100//max(n_neurons)
	max_w_size = neuron_size//2
	font = pygame.font.SysFont('Comic Sans MS', neuron_size)
	x_sep = (gui_x-x_offset*2)/max(n_layers-1,1)
	y_sep = (gui_y-y_offset*2)/max(max(n_neurons)-1,1)

	x_pos = [[x_offset+x_sep*l for _ in range(n_neurons[l])] for l in range(n_layers)]
	y_pos = [[y_offset+y_sep*n+(y_sep/2)*(max(n_neurons)-n_neurons[l]) for n in range(n_neurons[l])] for l in range(n_layers)]
	

	for l in range(n_layers-1):
		for n1 in range(n_neurons[l]):
			for n2 in range(n_neurons[l+1]):
				pos1 = (x_pos[l][n1],y_pos[l][n1])
				pos2 = (x_pos[l+1][n2],y_pos[l+1][n2])
				w = weights[l][n1][n2]
				if w == 0:
					pygame.draw.line(screen,(90,90,90),pos1,pos2,1)
				else:
					pygame.draw.line(screen,(200*(w<0),200*(w>0),50),pos1,pos2,max(min((int(round(w*max_w_size))),max_w_size),1))

	for n in range(n_neurons[0]):
		pygame.draw.circle(screen,(0,0,0),(x_pos[0][n],y_pos[0][n]),neuron_size)
		if inputs.shape!=(0,):
			pygame.draw.circle(screen,(255*(inputs[n]<0),255*(inputs[n]>0),0),(x_pos[0][n],y_pos[0][n]),round(abs(inputs[n])*neuron_size))
	for l in range(1,n_layers):
		for n in range(n_neurons[l]):
			x,y = x_pos[l][n],y_pos[l][n]
			b = biases[l-1][n]
			pygame.draw.circle(screen,(0,0,200),(x,y),neuron_size)
			b = round(b,2)
			text = font.render(str(b), False, (200*(b<0),200*(b>0),0))
			screen.blit(text, text.get_rect(center=(x,y+neuron_size+10)))
			if outputs.shape!=(0,) and l == n_layers-1:
				pygame.draw.circle(screen,(255*(outputs[n]<0),255*(outputs[n]>0),0),(x,y),round(abs(outputs[n])*neuron_size))

	
# neurons = [5,3,2]
# weights = [np.random.rand(neurons[i],neurons[i+1]) for i in range(len(neurons)-1)]
# biases = [np.random.rand(neurons[i]) for i in range(1,len(neurons))]

# inputs = np.array([.5,1,-.3,.2,0])
# outputs = np.array([.5,-.3])

# pygame.init()
# screen = pygame.display.set_mode((1000,1000))

# running = True
# while running:
# 	for event in pygame.event.get():
# 		if event.type == pygame.QUIT:
# 			running = False
# 	visualize(screen,weights,biases,inputs,outputs)
# 	pygame.display.update()