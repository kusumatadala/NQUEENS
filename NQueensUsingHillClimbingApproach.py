# -*- coding: utf-8 -*-
"""
Created on Thu Sep  1 15:17:10 2022

@author: Kusuma

Purpose: Prints an arrangement of 'n' queens on n*n board such that no two queens attack each other.
"""
from random import randint

   
def generaterboard(n):
    """
    Parameters
    ----------
    n : INTEGER
        Number of queens.

    Returns
    -------
    m : Integer array
        m[i]=number of row in which the queen is placed in i th column in the board.

    """
    m=[]
    for i in range(n):
        q=randint(0,n-1)
        m.append(q)
        m=[1,7,4,8,0,9,1,5,2,6]
    return m
      
def solve(board):
    """

    Parameters
    ----------
    board : Integer Array
         board[i]=number of the row in which the queen is placed in i th column.

    Prints
    -------
    goal arrangement.

    """
    cur=board
    cost=heuristic(board)
    while(cost!=0):
        cur=bestneighbour(board,cost)
        if(cur==None):
            generaterboard(board)
            cur=board
        cost=heuristic(cur)
    print_(cur)
def heuristic(board):
    """
    

    Parameters
    ----------
    board :  Integer Array
         board[i]=number of the row in which the queen is placed in i th column.

    Returns
    -------
    d : Integer
        Number of queens attacking each other.

    """
    d=0
    n=len(board)
    for k in range(n):
        i,j=k,board[k]
        for l in range(k+1,n):
            p,q=l,board[l]
            if(q==j or (i+j)==(p+q) or (j-i)==(q-p)):
                d+=1
    return d
def print_(m):
    """
    

    Parameters
    ----------
    m : Integer Array
         m[i]=number of row in which the queen is placed in i th column in the board.

    Prints
    -------
     m : Matrix of size n*n containing '-','Q',
        an arrangement of 'n' queens across n*n board such that no queens attack each other

    """
    n=len(m)
    for i in range(n):
        for j in range(n):
            if(m[i]==j):
                print("Q",end=" ")
            else:
                print("_",end=" ")
        print()

def bestneighbour(board,cost):
    """
    

    Parameters
    ----------
    board : Integer array
             board[i]=number of the row in which the queen is placed in i th column.
    cost : Integer
           Number of queens attacking each other.

    Returns
    -------
    ans : Integer array or None
        an arrangement generated after displacing a single queen
        from the board in the same in the same column only with minimum heuristic
        if the minimum heuristic is grater than board returns None.

    """
    mini=cost
    ans=None
    n=len(board)
    for i in range(n):
        temp=board[i]
        for j in range(n):
            board[i]=j
            cost=heuristic(board)
            if(cost<mini):
                ans=board.copy()
        board[i]=temp
    return ans
                
                
if __name__=="__main__":
    print("enter n:")
    n=int(input())
    b=generaterboard(n)
    solve(b)