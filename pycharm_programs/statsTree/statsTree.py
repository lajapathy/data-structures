#!/usr/bin/python

from StatsTreeNode import StatsTreeNode
import re, sys
from stack import stack
import argparse

# Global variables
gPrevLevel = 0
gStackObj = stack()
gRootNodeName = 'pgw-stats'
# Keep root node as global
rootTreeNode = StatsTreeNode(gRootNodeName)
gLastNodePushedToStack = False
gLastLineTwoColumn = False
gPrevLeftParentNodeStack = stack()
gPrevRightParentNodeStack = stack()
gNested2ColumnScenario = False
gPathList = []
gPathString = ''
global gStatsFp
gTreeDict = {}
gGroupStatsFlag = False
gGroupChildDict = {}
twoColumnHeadingScenario = False


def argParse():
    global gStatsFp
    global gPathList
    global gPathString
    global gGroupStatsFlag
    parserObj = argparse.ArgumentParser()
    parserObj.add_argument("-s", "--statsfile", dest="statsfile", help="Stats file")
    parserObj.add_argument("-p", "--pathlist", dest="path",
                           help="Details of the statistics needed. Ex: pgw-stats,Total EMM Control Messages,Sent,Retransmissions")
    parserObj.add_argument("-g", "--groupStats", dest="groupStatsFlag",
                           help="This flag tells whether we need a group of stats or a single one", action='store_true')
    args = parserObj.parse_args()
    if (not args.statsfile or (not args.path)):
        print 'Mandatory arguments missing'
        print 'For Usage help : ./stats_tree.py -h'
        sys.exit(3)
    gStatsFp = open(args.statsfile, 'r')
    gPathString = args.path + ','
    gPathList = args.path.split(',')
    gGroupStatsFlag = args.groupStatsFlag


def two_column_scenario(line, level):
    global gLastNodePushedToStack
    global gStackObj
    global gPrevLevel
    global gLastLineTwoColumn
    global gPrevLeftParentNodeStack
    global gPrevRightParentNodeStack
    global gNested2ColumnScenario
    global twoColumnHeadingScenario
    if re.match('^\s*(\S+.*):\s*(\S+)\s+(\S+.*):\s*(\S+)', line):
        matchObj = re.match('^\s*(\S+.*?):\s*(\S+)\s+(\S+.*?):\s*(\S+)', line)
        nodeName = matchObj.group(1)
        currLevel = level

    elif twoColumnHeadingScenario:
        if re.match('^\s*(\S+.*):\s*(\S+.*):\s*$', line):
            matchObj = re.match('^\s*(\S+.*):\s*(\S+.*):\s*', line)
        nodeName = matchObj.group(1)
        currLevel = level

    if level == gPrevLevel:
        if gNested2ColumnScenario:
            parentNodeName = gStackObj.peek()
            varNode = StatsTreeNode(nodeName)
            add_node_to_tree(varNode, getParentNode(parentNodeName))
            nested2ColumnScenario(line, level)
            gPrevLevel = currLevel
            gLastLineTwoColumn = True
            return
        # if gLastNodePushedToStack:
        gStackObj.pop()
        # Make note of topmost stack entry as parent
        parentNodeName = gStackObj.peek()
        # Push current node to stack.
        gStackObj.push(nodeName)

    if level == (gPrevLevel + 1):
        # We are one level deeper
        # Handling SPECIAL case scenario - NESTED 2 COLUMNS scenario
        # Check if previous line was a two-column scenario. If yes, we have hit the above special case scenario
        if gLastLineTwoColumn:
            parentNodeName = gStackObj.peek()
            varNode = StatsTreeNode(nodeName)
            add_node_to_tree(varNode, getParentNode(parentNodeName))
            nested2ColumnScenario(line, level)
            gPrevLevel = currLevel
            gLastLineTwoColumn = True
            return
        parentNodeName = gStackObj.peek()
        gStackObj.push(nodeName)
        gLastNodePushedToStack = True

    if level < gPrevLevel:
        gNested2ColumnScenario = False
        # We are atleast one level shallow
        # See how shallow we have come and pop items from the stack
        popCount = gPrevLevel - level
        for i in xrange(popCount):
            gStackObj.pop()
        parentNodeName = gStackObj.peek()
        gStackObj.push(nodeName)
        gLastNodePushedToStack = True
    if not twoColumnHeadingScenario:
        statsValue = matchObj.group(2)
        # Create a node for the stats value (with no parent)
        statsNode = StatsTreeNode(statsValue)
        varNode = StatsTreeNode(nodeName)
        varNode.addChild(statsNode)
    else:
        varNode = StatsTreeNode(nodeName)
    # Add this node as a child to the variable node
    # Make note of the previous left parent node
    gPrevLeftParentNodeStack.push(varNode)
    add_node_to_tree(varNode, getParentNode(parentNodeName))
    # Repeat same for second column
    if not twoColumnHeadingScenario:
        nodeName = matchObj.group(3)
        statsValue = matchObj.group(4)
        statsNode = StatsTreeNode(statsValue)
        varNode = StatsTreeNode(nodeName)
        # Add this node as a child to the variable node
        varNode.addChild(statsNode)
    else:
        statsValue = 'NA'
        nodeName = matchObj.group(2)
        varNode = StatsTreeNode(nodeName)
    # Parent node will remain same as the first column
    # Make note of the previous right parent node
    gPrevRightParentNodeStack.push(varNode)
    add_node_to_tree(varNode, getParentNode(parentNodeName))
    gPrevLevel = currLevel
    gLastLineTwoColumn = True
    twoColumnHeadingScenario = False


def one_column_scenario(line, level):
    global gStackObj
    global gPrevLevel
    global gLastNodePushedToStack
    global gNested2ColumnScenario
    global gLastLineTwoColumn
    gNested2ColumnScenario = False
    if re.match('^\s*(\S+.*?):\s*(\S+)\s*', line):
        matchObj = re.match('^\s*(\S+.*?):\s*(\S+)\s*', line)
        nodeName = matchObj.group(1)
        statsValue = matchObj.group(2)
        currLevel = level
        if level == gPrevLevel:
            gStackObj.pop()
            # Make note of topmost stack entry as parent
            parentNodeName = gStackObj.peek()
            # Push current node to stack.
            gStackObj.push(nodeName)
            gLastNodePushedToStack = True
        if level == (gPrevLevel + 1):
            # We are one level deeper
            parentNodeName = gStackObj.peek()
            gStackObj.push(nodeName)
            gLastNodePushedToStack = True
        if level < gPrevLevel:
            # We are atleast one level shallow
            # See how shallow we have come and pop items from the stack
            popCount = gPrevLevel - level
            for i in xrange(popCount + 1):
                gStackObj.pop()
            parentNodeName = gStackObj.peek()
            gStackObj.push(nodeName)
            gLastNodePushedToStack = True
        statsNode = StatsTreeNode(statsValue)
        # Add this node as a child to the variable node
        varNode = StatsTreeNode(nodeName)
        varNode.addChild(statsNode)
        add_node_to_tree(varNode, getParentNode(parentNodeName))
        gPrevLevel = currLevel
        gLastLineTwoColumn = False


def heading_scenario(line, level):
    global gLastNodePushedToStack
    global gStackObj
    global gPrevLevel
    global gNested2ColumnScenario
    global gLastLineTwoColumn
    gNested2ColumnScenario = False
    if level == 1:
        nodeName = re.match('^(\S+.*):.*$', line).group(1)
    if level == 2:
        nodeName = re.match('^\s{2}(\S+.*):.*$', line).group(1)
    if level == 3:
        nodeName = re.match('^\s{4}(\S+.*):.*', line).group(1)
    if (level == 1) and (gPrevLevel != 0):
        # We have went back to the starting level
        # Empty stack
        gStackObj.emptyContents()
        # parent node will be rootTreeNode
        gStackObj.push(rootTreeNode.data)
        gLastNodePushedToStack = True
        parentNodeName = gStackObj.peek()
        gStackObj.push(nodeName)

    elif level < gPrevLevel:
        # We are atleast one level shallow
        # See how shallow we have come and pop items from the stack
        popCount = gPrevLevel - level
        for i in xrange(popCount + 1):
            gStackObj.pop()
        parentNodeName = gStackObj.peek()
        gStackObj.push(nodeName)
        gLastNodePushedToStack = True
    elif level == gPrevLevel:
        # We are at same level. Do not add or remove anything from the stack
        parentNodeName = gStackObj.peek()
        gLastNodePushedToStack = False
    elif level == (gPrevLevel + 1):
        # One level deeper.
        parentNodeName = gStackObj.peek()
        gStackObj.push(nodeName)
        gLastNodePushedToStack = True
    currLevel = level
    node = StatsTreeNode(nodeName)
    add_node_to_tree(node, rootTreeNode.find(parentNodeName))
    gPrevLevel = currLevel
    gLastLineTwoColumn = False


def nested2ColumnScenario(line, level):
    global gNested2ColumnScenario
    global gPrevLeftParentNodeStack
    global gPrevRightParentNodeStack
    global gPrevLevel
    global gStackObj
    global gLastNodePushedToStack
    gNested2ColumnScenario = True
    sameLevelFlag = False
    if re.match('^\s*(\S+.*):\s*(\S+)\s+(\S+.*):\s*(\S+)', line):
        matchObj = re.match('^\s*(\S+.*?):\s*(\S+)\s+(\S+.*?):\s*(\S+)', line)
        nodeName = matchObj.group(1)
        statsValue = matchObj.group(2)
        currLevel = level
        if level == gPrevLevel:
            gStackObj.pop()
            # Push current node to stack.
            gStackObj.push(nodeName)
            sameLevelFlag = True
        if level == (gPrevLevel + 1):
            # We are one level deeper
            gStackObj.push(nodeName)
            gLastNodePushedToStack = True
            sameLevelFlag = False
        # Create a node for the stats value (with no parent)
        statsNode = StatsTreeNode(statsValue)
        # Add this node as a child to the variable node
        varNode = StatsTreeNode(nodeName)
        varNode.addChild(statsNode)
        # Make note of the previous left parent node
        parentNode = gPrevLeftParentNodeStack.peek()
        add_node_to_tree(varNode, parentNode)
        # Repeat same for second column
        nodeName = matchObj.group(3)
        statsValue = matchObj.group(4)
        # Parent node will remain same as the first column
        statsNode = StatsTreeNode(statsValue)
        # Add this node as a child to the variable node
        varNode = StatsTreeNode(nodeName)
        varNode.addChild(statsNode)
        parentNode = gPrevRightParentNodeStack.peek()
        add_node_to_tree(varNode, parentNode)
        gPrevLevel = currLevel
        gLastLineTwoColumn = True


def getParentNode(parentName):
    global gStackObj
    global rootTreeNode
    # There will be multiple parents with the same name. To get the right parent, we make use of the gStackObj.
    root2Parent = list(gStackObj.returnList())
    # Deleting first element, which is nothing but name of the rootTreeNode
    root2ParentLength = len(root2Parent)
    # del root2Parent[root2ParentLength-1]
    tempNode1 = rootTreeNode.find(root2Parent[0])
    for i in xrange(1, root2ParentLength):
        tempNode2 = tempNode1.find(root2Parent[i])
        try:
            if tempNode2.data == parentName:
                # We have found our parent
                return tempNode2
            else:
                tempNode1 = tempNode2
        except AttributeError, e:
            print 'Parent node \"' + str(root2Parent[i]) + '\" not found. Something wrong !! Aborting'
            sys.exit(3)


def add_node_to_tree(node, parentNode=rootTreeNode):
    global rootTreeNode
    # Add child nodeName to parent rootNode
    if not rootTreeNode.find(parentNode.data):
        print 'ERROR ! Parent node \"' + parentNode.data + '\" not found. Aborting'
        sys.exit(3)
    else:
        child_id = parentNode.addChild(node)
        node.parent = parentNode
        return node, child_id


def parse_stats_output(fp):
    global gStackObj
    global twoColumnHeadingScenario
    # Initially we set parent node to rootNode
    gStackObj.push('pgw-stats')
    # rootNode doesnt have a parent
    for line in fp:
        # Check if the given line is a STATS line in level 3
        # Two Column special case heading scenario
        # Ex:     Inter SGSN handover:                    Inter SGW handover:
        if re.match('^\s{2}(\S+.*):\s*(\S+.*):\s*$', line):
            twoColumnHeadingScenario = True
            two_column_scenario(line, 2)
            continue
        if re.match('^\s{4}(\S+.*):\s*(\S+.*):\s*$', line):
            twoColumnHeadingScenario = True
            two_column_scenario(line, 3)
            continue
        if re.match('^\s{6}(\S+.*):\s*(\S+.*):\s*$', line):
            twoColumnHeadingScenario = True
            two_column_scenario(line, 4)
            continue
        if re.match('^\s{8}(\S+.*):\s*(\S+.*):\s*$', line):
            twoColumnHeadingScenario = True
            two_column_scenario(line, 5)
            continue
        if re.match('^\s{10}(\S+.*):\s*(\S+.*):\s*$', line):
            twoColumnHeadingScenario = True
            two_column_scenario(line, 6)
            continue

        # Two column Level 2 scenario
        if re.match('^\s{2}(\S+.*):\s*(\S+)\s+(\S+.*):\s*(\S+)', line):
            two_column_scenario(line, 2)
            continue
        # Two column Level 3 scenario
        if re.match('^\s{4}(\S+.*):\s*(\S+)\s+(\S+.*):\s*(\S+)', line):
            two_column_scenario(line, 3)
            continue
        # Two column Level 4 scenario
        if re.match('^\s{6}(\S+.*):\s*(\S+)\s+(\S+.*):\s*(\S+)', line):
            two_column_scenario(line, 4)
            continue
        # Two column Level 5 scenario
        if re.match('^\s{8}(\S+.*):\s*(\S+)\s+(\S+.*):\s*(\S+)', line):
            two_column_scenario(line, 5)
            continue
        # Two column Level 6 scenario
        if re.match('^\s{10}(\S+.*):\s*(\S+)\s+(\S+.*):\s*(\S+)', line):
            two_column_scenario(line, 6)
            continue
        # One column Level 2 scenario
        if re.match('^\s{2}(\S+.*):\s*(\S+)\s*', line):
            one_column_scenario(line, 2)
            continue
        # One column Level 3 scenario
        if re.match('^\s{4}(\S+.*):\s*(\S+)\s*', line):
            one_column_scenario(line, 3)
            continue
        # One column Level 4 scenario
        if re.match('^\s{6}(\S+.*):\s*(\S+)\s*', line):
            one_column_scenario(line, 4)
            continue
        # One column Level 5 scenario
        if re.match('^\s{8}(\S+.*):\s*(\S+)\s*', line):
            one_column_scenario(line, 5)
            continue
        # One column Level 6 scenario
        if re.match('^\s{10}(\S+.*):\s*(\S+)\s*', line):
            one_column_scenario(line, 6)
            continue
        # Check if the given line is a heading line and level 1 Ex. SCTP Statistics:
        if re.match('^(\S+.*):.*$', line):
            heading_scenario(line, 1)
            continue
        # Check if the given line is a heading line and level 2 Ex: Transmitted SCTP Data:
        if re.match('^\s{2}(\S+.*):.*$', line):
            heading_scenario(line, 2)
            continue
        # Check if the given line a heading line in level 3
        if re.match('^\s{4}(\S+.*):.*', line):
            heading_scenario(line, 3)
            continue
        # Check if the given line a heading line in level 4
        if re.match('^\s{6}(\S+.*):.*', line):
            heading_scenario(line, 4)
            continue
        # Check if the given line a heading line in level 5
        if re.match('^\s{8}(\S+.*):.*', line):
            heading_scenario(line, 5)
            continue
        # Check if the given line a heading line in level 6
        if re.match('^\s{10}(\S+.*):.*', line):
            heading_scenario(line, 6)
            continue


def print_tree(startNode, parentData=''):
    if not startNode.getChildren():
        print parentData + startNode.data
        return
    else:
        for c in startNode.getChildren():
            print_tree(c, parentData + startNode.data + ' -> ')


def store_tree_dict(startNode, parentData=''):
    global gTreeDict
    if not startNode.getChildren():
        gTreeDict[parentData.replace(' -> ', ',')] = startNode.data
        return
    else:
        for c in startNode.getChildren():
            store_tree_dict(c, parentData + startNode.data + ' -> ')


def getDesiredNode(node=rootTreeNode, i=1):
    if i == len(gPathList):
        return node.getChildren()
    for child in node.getChildren():
        if child.data == gPathList[i]:
            return getDesiredNode(child, i + 1)


def traverseTree():
    global gGroupChildDict
    for child in getDesiredNode():
        '''			This try block is for a special case, like for example:
pgw-stats -> PDNs By Emergency-Type -> Emergency PDNs -> Setup -> 2000  >>>>>>>>>>>>>>>>>>>>>>>>>
pgw-stats -> PDNs By Emergency-Type -> Emergency PDNs -> Setup -> Authentic IMSI -> 2000
pgw-stats -> PDNs By Emergency-Type -> Emergency PDNs -> Setup -> Un-Authentic IMSI -> 0
pgw-stats -> PDNs By Emergency-Type -> Emergency PDNs -> Setup -> Only IMEI -> 0
        '''
        try:
            gGroupChildDict[child.data] = child.getChildren()[0].data
        except IndexError, e:
            gGroupChildDict[child.data] = 'NA'


argParse()
parse_stats_output(gStatsFp)
# print_tree(rootTreeNode)
if gGroupStatsFlag:
    traverseTree()
    print gGroupChildDict
else:
    store_tree_dict(rootTreeNode)
    print gTreeDict[gPathString]
    # print traverseTree()