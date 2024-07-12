# %%
# Graph families from Theorem 6

def Family1(hole1, hole2):
    if hole1 < 4 or hole2 < 4: raise ValueError("Holes must have size at least 4")

    G = Graph(hole1 + hole2 - 1)
    
    G.add_cycle(range(0, hole1))
    G.add_cycle(range(hole1 - 1, len(G)))

    return G

def Family2(hole1, hole2):
    if hole1 < 4 or hole2 < 4: raise ValueError("Holes must have size at least 4")

    G = Graph(hole1 + hole2 - 2)
    G.add_cycle(range(0, hole1))
    G.add_cycle(range(hole1 - 2, len(G)))

    return G

def Family3(hole1, hole2, centralpath):
    if hole1 < 4 or hole2 < 4: raise ValueError("Holes must have size at least 4")
    elif centralpath < 2: raise ValueError("Central path must have length at least 2")

    G = Graph(hole1 + hole2 + centralpath - 2)

    G.add_cycle(range(0, hole1))
    G.add_cycle(range(hole1 + centralpath - 2, len(G)))
    G.add_path(range(hole1-1, hole1 + centralpath - 1))

    return G

def Family4a(hole1, hole2):
    if hole1 < 4 or hole2 < 4: raise ValueError("Holes must have size at least 4")

    G = Graph(hole1 + hole2 + 1)
    n = len(G)-1

    G.add_cycle(range(0, hole1))
    G.add_cycle(range(hole1, n))
    G.add_edges(([n,0],[n,1],[n,n-1],[n,n-2]))

    return G

def Family4b(hole1, hole2):
    if hole1 < 4 or hole2 < 4: raise ValueError("Holes must have size at least 4")

    G = Graph(hole1 + hole2 + 1)
    n = len(G)-1

    G.add_cycle(range(0, hole1))
    G.add_cycle(range(hole1, n))
    G.add_edges(([n,0],[n,1]))

    for v in range(hole1, n):
        G.add_edge([n,v])

    return G

def Family4c(hole1, hole2):
    if hole1 < 4 or hole2 < 4: raise ValueError("Holes must have size at least 4")

    G = Graph(hole1 + hole2 + 1)
    n = len(G)-1

    G.add_cycle(range(0, hole1))
    G.add_cycle(range(hole1, n))

    for v in range(0, n):
        G.add_edge([n,v])

    return G

def Family5a(hole1, hole2, centralpath):
    if hole1 < 4 or hole2 < 4: raise ValueError("Holes must have size at least 4")
    elif centralpath < 2: raise ValueError("Central path must have length at least 2")

    G = Graph(hole1 + hole2 + centralpath)

    G.add_cycle(range(0, hole1))
    G.add_cycle(range(hole1 + centralpath, len(G)))
    G.add_path(range(hole1, hole1 + centralpath))

    G.add_edges(([hole1,0],[hole1,1],[hole1 + centralpath - 1, len(G)-1],[hole1 + centralpath - 1, len(G)-2]))

    return G

def Family5b(hole1, hole2, centralpath):
    if hole1 < 4 or hole2 < 4: raise ValueError("Holes must have size at least 4")
    elif centralpath < 2: raise ValueError("Central path must have length at least 2")

    G = Graph(hole1 + hole2 + centralpath)

    G.add_cycle(range(0, hole1))
    G.add_cycle(range(hole1 + centralpath, len(G)))
    G.add_path(range(hole1, hole1 + centralpath))

    G.add_edges(([hole1,0],[hole1,1]))

    for v in range(hole1 + centralpath, len(G)):
        G.add_edge([hole1 + centralpath - 1,v])

    return G

def Family5c(hole1, hole2, centralpath):
    if hole1 < 4 or hole2 < 4: raise ValueError("Holes must have size at least 4")
    elif centralpath < 2: raise ValueError("Central path must have length at least 2")

    G = Graph(hole1 + hole2 + centralpath)

    G.add_cycle(range(0, hole1))
    G.add_cycle(range(hole1 + centralpath, len(G)))
    G.add_path(range(hole1, hole1 + centralpath))

    for v in range(0, hole1):
        G.add_edge([hole1,v])

    for v in range(hole1 + centralpath, len(G)):
        G.add_edge([hole1 + centralpath - 1,v])

    return G

def Family6a(hole1, hole2):
    if hole1 < 4 or hole2 < 4: raise ValueError("Holes must have size at least 4")

    G = Graph(hole1 + hole2)

    G.add_cycle(range(0, hole1))
    G.add_cycle(range(hole1, len(G)))

    G.add_edges(([0,len(G)-1],[0,len(G)-2]))

    return G

def Family6b(hole1, hole2):
    if hole1 < 4 or hole2 < 4: raise ValueError("Holes must have size at least 4")

    G = Graph(hole1 + hole2)

    G.add_cycle(range(0, hole1))
    G.add_cycle(range(hole1, len(G)))

    for v in range(hole1, len(G)):
        G.add_edge([0,v])

    return G

def Family7a(hole1, hole2, centralpath):
    if hole1 < 4 or hole2 < 4: raise ValueError("Holes must have size at least 4")
    elif centralpath < 2: raise ValueError("Central path must have length at least 2")

    G = Graph(hole1 + hole2 + centralpath - 1)

    G.add_cycle(range(0, hole1))
    G.add_cycle(range(hole1 + centralpath - 1, len(G)))
    G.add_path(range(hole1-1, hole1 + centralpath - 1))

    G.add_edges(([hole1 + centralpath - 2, len(G)-1], [hole1 + centralpath - 2, len(G)-2]))
    
    return G

def Family7b(hole1, hole2, centralpath):
    if hole1 < 4 or hole2 < 4: raise ValueError("Holes must have size at least 4")
    elif centralpath < 2: raise ValueError("Central path must have length at least 2")

    G = Graph(hole1 + hole2 + centralpath - 1)

    G.add_cycle(range(0, hole1))
    G.add_cycle(range(hole1 + centralpath - 1, len(G)))
    G.add_path(range(hole1-1, hole1 + centralpath - 1))
    
    for v in range(hole1 + centralpath - 1, len(G)):
        G.add_edge([hole1 + centralpath - 2,v])
    
    return G

def Family8a(hole1, hole2):
    if hole1 < 4 or hole2 < 4: raise ValueError("Holes must have size at least 4")

    G = Graph(hole1 + hole2 - 1)
    
    G.add_cycle(range(0, hole1))
    G.add_cycle(range(hole1 - 1, len(G)))

    G.add_edge(0,len(G)-1)

    return G

def Family8b(hole1, hole2):
    if hole1 < 4 or hole2 < 4: raise ValueError("Holes must have size at least 4")

    G = Graph(hole1 + hole2 - 1)
    
    G.add_cycle(range(0, hole1))
    G.add_cycle(range(hole1 - 1, len(G)))

    G.add_edges(([0,len(G)-1],[0,hole1]))

    return G

def Family8c(hole1, hole2):
    if hole1 < 4 or hole2 < 4: raise ValueError("Holes must have size at least 4")

    G = Graph(hole1 + hole2 - 1)
    
    G.add_cycle(range(0, hole1))
    G.add_cycle(range(hole1 - 1, len(G)))

    for v in range(hole1 - 1, len(G)):
        G.add_edge([0,v])

    return G

def Family8d(hole1, hole2):
    if hole1 < 4 or hole2 < 4: raise ValueError("Holes must have size at least 4")

    G = Graph(hole1 + hole2 - 1)
    
    G.add_cycle(range(0, hole1))
    G.add_cycle(range(hole1 - 1, len(G)))

    for v in range(hole1 - 1, len(G)):
        G.add_edge([0,v])

    G.add_edge([len(G)-1,hole1-2])

    return G

def Family8e(hole1, hole2):
    if hole1 < 4 or hole2 < 4: raise ValueError("Holes must have size at least 4")

    G = Graph(hole1 + hole2 - 1)
    
    G.add_cycle(range(0, hole1))
    G.add_cycle(range(hole1 - 1, len(G)))

    for v in range(hole1 - 1, len(G)):
        G.add_edge([0,v])

    for v in range(0, hole1):
        G.add_edge([len(G)-1,v])
    
    return G


def Family9a(hole1, hole2):
    if hole1 < 4 or hole2 < 4: raise ValueError("Holes must have size at least 4")

    G = Graph(hole1 + hole2)
    
    G.add_cycle(range(0, hole1))
    G.add_cycle(range(hole1, len(G)))

    G.add_edges(([0,hole1],[hole1-1,len(G)-1],[0,len(G)-1]))

    return G

def Family9b(hole1, hole2):
    if hole1 < 4 or hole2 < 4: raise ValueError("Holes must have size at least 4")

    G = Graph(hole1 + hole2)
    
    G.add_cycle(range(0, hole1))
    G.add_cycle(range(hole1, len(G)))

    G.add_edges(([0,hole1],[hole1-1,len(G)-1],[0,len(G)-1]))

    for v in range(hole1, len(G)):
        G.add_edge([0,v])

    return G

def Family9c(hole1, hole2):
    if hole1 < 4 or hole2 < 4: raise ValueError("Holes must have size at least 4")

    G = Graph(hole1 + hole2)
    
    G.add_cycle(range(0, hole1))
    G.add_cycle(range(hole1, len(G)))

    G.add_edges(([0,hole1],[hole1-1,len(G)-1],[0,len(G)-1]))

    for v in range(hole1, len(G)):
        G.add_edge([0,v])

    for v in range(0, hole1):
        G.add_edge([len(G)-1,v])

    return G

def Family10a(hole1, hole2):
    if hole1 < 4 or hole2 < 4: raise ValueError("Holes must have size at least 4")

    G = Graph(hole1 + hole2)
    
    G.add_cycle(range(0, hole1))
    G.add_cycle(range(hole1, len(G)))

    G.add_edges(([0,hole1],[hole1-1,len(G)-1],[0,len(G)-1],[hole1-1,hole1]))

    return G

def Family10b(hole1, hole2):
    if hole1 < 4 or hole2 < 4: raise ValueError("Holes must have size at least 4")

    G = Graph(hole1 + hole2)
    
    G.add_cycle(range(0, hole1))
    G.add_cycle(range(hole1, len(G)))

    G.add_edges(([0,hole1],[hole1-1,len(G)-1],[0,len(G)-1],[hole1-1,hole1]))

    for v in range(hole1, len(G)):
        G.add_edge([0,v])

    return G

def Family10c(hole1, hole2):
    if hole1 < 4 or hole2 < 4: raise ValueError("Holes must have size at least 4")

    G = Graph(hole1 + hole2)
    
    G.add_cycle(range(0, hole1))
    G.add_cycle(range(hole1, len(G)))

    G.add_edges(([0,hole1],[hole1-1,len(G)-1],[0,len(G)-1],[hole1-1,hole1]))

    for v in range(hole1, len(G)):
        G.add_edge([0,v])
        G.add_edge([hole1-1,v])

    return G

def Family10d(hole1, hole2):
    if hole1 < 4 or hole2 < 4: raise ValueError("Holes must have size at least 4")

    G = Graph(hole1 + hole2)
    
    G.add_cycle(range(0, hole1))
    G.add_cycle(range(hole1, len(G)))

    G.add_edges(([0,hole1],[hole1-1,len(G)-1],[0,len(G)-1],[hole1-1,hole1]))

    for v in range(hole1, len(G)):
        G.add_edge([0,v])
    
    for v in range(0, hole1):
        G.add_edge([len(G)-1,v])

    return G

def Family10e(hole1, hole2):
    if hole1 < 4 or hole2 < 4: raise ValueError("Holes must have size at least 4")

    G = Graph(hole1 + hole2)
    
    G.add_cycle(range(0, hole1))
    G.add_cycle(range(hole1, len(G)))

    G.add_edges(([0,hole1],[hole1-1,len(G)-1],[0,len(G)-1],[hole1-1,hole1]))

    for v in range(hole1, len(G)):
        G.add_edge([0,v])
        G.add_edge([hole1-1,v])
    
    for v in range(0, hole1):
        G.add_edge([len(G)-1,v])

    return G

def Family10f(hole1, hole2):
    if hole1 < 4 or hole2 < 4: raise ValueError("Holes must have size at least 4")

    G = Graph(hole1 + hole2)
    
    G.add_cycle(range(0, hole1))
    G.add_cycle(range(hole1, len(G)))

    G.add_edges(([0,hole1],[hole1-1,len(G)-1],[0,len(G)-1],[hole1-1,hole1]))

    for v in range(hole1, len(G)):
        G.add_edge([0,v])
        G.add_edge([hole1-1,v])
    
    for v in range(0, hole1):
        G.add_edge([len(G)-1,v])
        G.add_edge([hole1,v])

    return G

# Additional families from disconnected case

def Family0(hole1, hole2):
    if hole1 < 4 or hole2 < 4: raise ValueError("Holes must have size at least 4")

    G = Graph(hole1 + hole2)
    
    G.add_cycle(range(0, hole1))
    G.add_cycle(range(hole1, len(G)))

    return G

# %%
import itertools

def AllFamilies(maxhole, maxpath, connected = True):
    # Output a list of all graphs from all families up to a certain sized hole

    if maxhole < 4: raise ValueError("Holes must have size at least 4")
    elif maxpath < 2: raise ValueError("Central path must have length at least 2")

    graphlist = []

    # Add symmetric families
    for r in range(4,maxhole+1):
        for l in range(4,r+1):
            graphlist.append([Family1(l,r),Family2(l,r),Family8a(l,r),Family8e(l,r),Family9a(l,r),Family9c(l,r),Family10a(l,r),Family10d(l,r),Family10f(l,r)])

            if connected: graphlist.append([Family4a(l,r), Family4c(l,r)])
            else: graphlist.append([Family0(l,r),Family3(l,r,2)])

            if connected: 
                for p in range(2,maxpath+1):
                    graphlist.append([Family3(l,r,p),Family5a(l,r,p),Family5c(l,r,p)])

    # Add asymmetric families
    for r in range(4,maxhole+1):
        for l in range(4,maxhole+1):
            graphlist.append([Family6a(l,r),Family6b(l,r),Family8b(l,r),Family8c(l,r),Family8d(l,r),Family9b(l,r),Family10b(l,r),Family10c(l,r),Family10e(l,r)])

            if connected: 
                graphlist.append([Family4b(l,r)])

                for p in range(2,maxpath+1):
                    graphlist.append([Family5b(l,r,p),Family7a(l,r,p),Family7b(l,r,p)])

    graphlist = list(itertools.chain.from_iterable(graphlist)) #Flatten list
    return graphlist



