#coding: utf-8
from bs4 import BeautifulSoup as BS

def get_depth(soup,attr):
    if hasattr(soup, attr) and soup.contents:
        return max([get_depth(child, attr) for child in soup.contents]) + 1
    else:
        return 0
def build_tree(soup,tag,sub_tag,title="principal",tree={},level=0):
    depth = level
    Titles_Tree = tree
    #On Cherche un DL
    Starting_Bazar = soup.find(tag)
    if Starting_Bazar is not None:
        #On n'est pas encore au bout d'un niveau
        #On prend les enfants de ce DL
        for child in Starting_Bazar.children:
            #Si on a un DT avec un H3, on a un nouveau titre de niveau
            if (child.find(tag) is not None):
                sub_title = child.h3.contents[0]
                #sub_title = Starting_Bazar.find(sub_tag).h3.contents[0]
                if depth in Titles_Tree:
                    Titles_Tree[depth].append([title,sub_title])
                else:
                    Titles_Tree[depth] = []
                    Titles_Tree[depth].append([title,sub_title])
                sub_depth = depth + 1
                build_tree(child,tag,sub_tag,sub_title,Titles_Tree,sub_depth)
    else:
        return Titles_Tree
    return Titles_Tree

def clean_tree(Tree):


def build_links(soup)



BookFile = open("C:\\Users\\Nicolas\\Documents\\favoris_02_01_2020.html",'r',encoding="utf8")
BookSoup = BS(BookFile,"html5lib")
Titres = {}
print(build_tree(BookSoup,'dl','dt',))
