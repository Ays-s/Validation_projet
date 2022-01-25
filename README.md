# Validation_projet

GUILLERMO Ayrwan, QUESTROY Hugo & LEDENTU Enzo
------
ENSTA Bretagne 3A

## Models
File  : hanoi.py  
* Classes : 
  * HConfig
  * Hanoi
* Functions : 
  * guard_def
  * action_def
  * hanoi_soup
  * is_accepted

File  : alicebob.py 
* Classes : 
  * ABConfig
* Functions : 
  * alice_guard_def
  * alice_action_def
  * alice_soup
  * alice_is_accepted
* Going to be upgraded

## Src
File  : graph.py  
* Classes : 
  * Graph
  * NFA

File  : kernel.py  
* Classes : 
  * TransitionRelation
  * AcceptingSet
  * IdentityProxy
  * ParentStoreProxy
  * SemanticTransitionRelation
  * STR2TR
  * IsAcceptingProxy

File : soup.py
* Classes :
  * Behavior
  * BehaviorSoup
  * BehaviorSoupSemantics

File  : node.py  
* Class : 
  * Node

## Tools
File  : algorithms.py  
* Methods : 
  * reachable_bfs
  * is_safe_bfs
  * find_accepting_bfs
  * get_trace
  * predicate_model_checker


## Installation / run

To run :
```shell
python main.py [hanoi/alice]
```
