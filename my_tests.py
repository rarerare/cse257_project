#!/usr/bin/env python
# coding: utf-8

# # Setup (should take < 100 seconds)

# In[1]:


get_ipython().system(u'apt-get update')
get_ipython().system(u'apt-get install libsdl2-gfx-dev libsdl2-ttf-dev')

# Make sure that the Branch in git clone and in wget call matches !!
get_ipython().system(u'git clone -b v2.9 https://github.com/google-research/football.git')
get_ipython().system(u'mkdir -p football/third_party/gfootball_engine/lib')

get_ipython().system(u'wget https://storage.googleapis.com/gfootball/prebuilt_gameplayfootball_v2.8.so -O football/third_party/gfootball_engine/lib/prebuilt_gameplayfootball.so')
get_ipython().system(u'cd football && GFOOTBALL_USE_PREBUILT_SO=1 python3 -m pip install .')



# In[2]:


import gfootball.env as football_env
import matplotlib.pyplot as plt
env = football_env.create_environment(env_name="academy_empty_goal", stacked=False, logdir='/tmp/football', write_goal_dumps=False, write_full_episode_dumps=False, render=False)
num_games=100
durations=[]

for i in range(num_games):
  env.reset()
  steps = 0
  while True:
    #if steps<20:
    #  obs, rew, done, info = env.step(5)
    #else:
    obs, rew, done, info = env.step(12)
    steps += 1
    #print(obs.shape)
    #if steps==20:

    #plt.imshow(obs[:,:,0])
    #plt.show()
    #plt.imshow(obs[:,:,1])
    #plt.show()
    #plt.imshow(obs[:,:,2])
    #plt.show()
    #plt.imshow(obs[:,:,3])
    #plt.show()
    #fig, axs = plt.subplots(1, 4)
    
    #if steps % 100 == 0:
    #print("Step %d Reward: %f" % (steps, rew))
    if done:
      break

  #print("Steps: %d Reward: %.2f" % (steps, rew))
  durations.append(steps)
plt.plot(durations)
plt.xlabel("game number")
plt.ylabel("times the agent shot goal")
plt.title("figure 2. shooting goal from medium distance")
plt.show()


# In[1]:


env = football_env.create_environment(env_name="academy_empty_goal_close", stacked=False, logdir='/tmp/football', write_goal_dumps=False, write_full_episode_dumps=False, render=False)
num_games=100
durations=[]

for i in range(num_games):
  env.reset()
  steps = 0
  while True:
    #if steps<20:
    #  obs, rew, done, info = env.step(5)
    #else:
    obs, rew, done, info = env.step(12)
    steps += 1
    #print(obs.shape)
    #if steps==20:

    #plt.imshow(obs[:,:,0])
    #plt.show()
    #plt.imshow(obs[:,:,1])
    #plt.show()
    #plt.imshow(obs[:,:,2])
    #plt.show()
    #plt.imshow(obs[:,:,3])
    #plt.show()
    #fig, axs = plt.subplots(1, 4)
    
    #if steps % 100 == 0:
    #print("Step %d Reward: %f" % (steps, rew))
    if done:
      break

  #print("Steps: %d Reward: %.2f" % (steps, rew))
  durations.append(steps)
plt.plot(durations)
plt.xlabel("game number")
plt.ylabel("times the agent shot goal")
plt.title("figure 1. shooting goal from close distance")
plt.show()

