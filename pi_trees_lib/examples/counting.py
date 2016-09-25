#!/usr/bin/env python

"""
    counting.py - Version 1.0 2013-09-22
    
    Perform a number of parallel counting tasks
    
    Created for the Pi Robot Project: http://www.pirobot.org
    Copyright (c) 2013 Patrick Goebel.  All rights reserved.

    This program is free software; you can redistribute it and/or modify
    it under the terms of the GNU General Public License as published by
    the Free Software Foundation; either version 2 of the License, or
    (at your option) any later version.
    
    This program is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU General Public License for more details at:
    
    http://www.gnu.org/licenses/gpl.html
"""

from pi_trees_lib.pi_trees_lib import *
import time

class CountingExample():
    def __init__(self):
        # The root node
        BEHAVE = Sequence("behave")
        
        PARALLEL_TASKS = ParallelOne("Counting in Parallel")
        
        COUNT2 = Count("Count+2", 1, 2, 1)
        COUNT5 = Count("Count-5", 5, 1, -1)
        COUNT16 = Count("Count+16", 1, 16, 1)

        PARALLEL_TASKS.add_child(COUNT5)
        PARALLEL_TASKS.add_child(COUNT2)
        PARALLEL_TASKS.add_child(COUNT16)
        
        BEHAVE.add_child(PARALLEL_TASKS)
                
        print "Behavior Tree Structure"
        print_tree(BEHAVE)
            
        # Run the tree
        while True:
            status = BEHAVE.run()
            if status == TaskStatus.SUCCESS:
                print "Finished running tree."
                break
                
class Count(Task):
    def __init__(self, name, start, stop, step, *args, **kwargs):
        super(Count, self).__init__(name, *args, **kwargs)
        
        self.name = name
        self.start = start
        self.stop = stop
        self.step = step
        self.count = self.start
        print "Creating task Count", self.start, self.stop, self.step
 
    def run(self):
        if abs(self.count - self.stop - self.step) <= 0:
            return TaskStatus.SUCCESS
        else:
            print self.name, self.count
            time.sleep(0.5)
            self.count += self.step
            if abs(self.count - self.stop - self.step) <= 0:
                return TaskStatus.SUCCESS
            else:
                return TaskStatus.RUNNING

    
    def reset(self):
        self.count = self.start

if __name__ == '__main__':
    tree = CountingExample()

