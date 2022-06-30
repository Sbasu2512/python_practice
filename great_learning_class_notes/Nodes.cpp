#Proprietary content. ©Great Learning. All Rights Reserved. Unauthorized use or distribution prohibited

#include <iostream>
#include "Nodes.h"

using namespace std;

// Creates head node at initial position (head)
void CNodeList::CreateNode(int value){
	s_Node *nodeTemp = new s_Node;

	nodeTemp->Data = value;
	nodeTemp->NextNode = 0;

	// Linked list not created yet
	if (m_NodeHead == 0)
	{
		m_NodeHead = nodeTemp;
		m_NodeTail = nodeTemp;
		nodeTemp = 0;
	}
	else
	{
		m_NodeTail->NextNode = nodeTemp;
		m_NodeTail = nodeTemp;
	}
}

//Displays all the nodes
void CNodeList::DisplayNodes(){
	s_Node *nodeTemp = new s_Node;
	nodeTemp = m_NodeHead;
	//Display the nodes with a tab in between nodes
	while (nodeTemp != 0)
	{
		cout << nodeTemp->Data << "\t";
		nodeTemp = nodeTemp->NextNode;
	}

}

// insert node at start
void CNodeList::InsertNodeAtStart(int value) {
	s_Node *nodeTemp = new s_Node;
	nodeTemp->Data = value;
	nodeTemp->NextNode = m_NodeHead;
	m_NodeHead = nodeTemp;
}


// This function inserts the node at a given position
void CNodeList::InsertNodeAtPosition(int pos, int value) {
	s_Node *preNode = new s_Node;
	s_Node *curNode = new s_Node;
	s_Node *tempNode = new s_Node;
	curNode = m_NodeHead;
	// navigate to the position
	for (int i = 1; i < pos; i++)
	{
		preNode = curNode;
		curNode = curNode->NextNode;
	}
	// insert the node and change the links
	tempNode->Data = value;
	preNode->NextNode = tempNode;
	tempNode->NextNode = curNode;
}

//delete node at start
void CNodeList::DeleteNodeAtFirst() {
	s_Node *nodeTemp = new s_Node;
	nodeTemp = m_NodeHead;
	m_NodeHead = m_NodeHead->NextNode;
	//delete nodeTemp;
}


// delete node at end
void CNodeList::DeleteNodeAtLast() {
	s_Node *currentNode = new s_Node;
	s_Node *previousNode = new s_Node;
	currentNode = m_NodeHead;
	// navigate to the last node
	while (currentNode->NextNode != NULL)
	{
		previousNode = currentNode;
		currentNode = currentNode->NextNode;
	}
	m_NodeTail = previousNode;
	previousNode->NextNode = NULL;
	//delete currentNode;
}

// delete node at a given location
void CNodeList::DeleteNodeAtPosition(int pos) {
	s_Node *currentNode = new s_Node;
	s_Node *previousNode = new s_Node;
	currentNode = m_NodeHead;
	//navigate to the node location (pos)
	for (int i = 1; i < pos; i++)
	{
		previousNode = currentNode;
		currentNode = currentNode->NextNode;
	}
	previousNode->NextNode = currentNode->NextNode;
}

//Destroy all the nodes
void CNodeList::Destroy() {
	s_Node *currentNode = new s_Node;
	s_Node *previousNode = new s_Node;
	currentNode = m_NodeHead;
	while (currentNode->NextNode != 0)
	{
		previousNode = currentNode;
		currentNode = currentNode->NextNode;
		delete previousNode;
	}

}
