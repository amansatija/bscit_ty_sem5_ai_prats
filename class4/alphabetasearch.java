package com.core;
import java.util.*;

public class AlphaBetaSearch {
	    public static void main(String[] args) {
	        // Create the initial game state node
	        Node root = new Node("root");
	        
	        // Perform alpha-beta search
	        int result = alphaBeta(root, 3, Integer.MIN_VALUE, Integer.MAX_VALUE, true);
	        
	        // Print the result
	        System.out.println("Best score: " + result);
	    }

	    public static int alphaBeta(Node node, int depth, int alpha, int beta, boolean maximizingPlayer) {
	        if (depth == 0 || isTerminal(node)) {
	            return evaluate(node);
	        }

	        if (maximizingPlayer) {
	            int maxEval = Integer.MIN_VALUE;
	            for (Node child : getChildren(node)) {
	                int eval = alphaBeta(child, depth - 1, alpha, beta, false);
	                maxEval = Math.max(maxEval, eval);
	                alpha = Math.max(alpha, eval);
	                if (beta <= alpha) {
	                    break;
	                }
	            }
	            return maxEval;
	        } else {
	            int minEval = Integer.MAX_VALUE;
	            for (Node child : getChildren(node)) {
	                int eval = alphaBeta(child, depth - 1, alpha, beta, true);
	                minEval = Math.min(minEval, eval);
	                beta = Math.min(beta, eval);
	                if (beta <= alpha) {
	                    break;
	                }
	            }
	            return minEval;
	        }
	    }

	    private static boolean isTerminal(Node node) {
	        // Simple terminal condition for demonstration
	        return node.getName().equals("leaf");
	    }

	    private static int evaluate(Node node) {
	        // Simple evaluation function for demonstration
	        if (node.getName().equals("leaf")) {
	            return (int) (Math.random() * 100); // Random score
	        }
	        return 0;
	    }

	    private static List<Node> getChildren(Node node) {
	        // Simple child generation for demonstration
	        List<Node> children = new ArrayList<>();
	        if (!node.getName().equals("leaf")) {
	            children.add(new Node("leaf"));
	            children.add(new Node("non-leaf"));
	        }
	        return children;
	    }

	    // Node class representing the game state
	    public static class Node {
	        private String name;

	        public Node(String name) {
	            this.name = name;
	        }

	        public String getName() {
	            return name;
	        }

	        public void setName(String name) {
	            this.name = name;
	        }
	    }
	

}