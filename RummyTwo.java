/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package rummy;

import java.util.ArrayList;
import java.util.Collections;
import java.util.List;
import java.util.concurrent.ThreadLocalRandom;

/**
 *
 * @author Manvi Agarwal
 */
public class RummyTwo {
    
    public static void main(String[] args) {
        
        List<Integer> deck = new ArrayList<>();
    	List<Integer> playerMHand = new ArrayList<>();
    	List<Integer> playerVHand = new ArrayList<>();
    	List<Integer> drawPile = new ArrayList<>();
    	List<Integer> discardPile = new ArrayList<>();
   	 
    	//POPULATING THE DECK
    	boolean add;
    	int min = 1;
    	int max = 6;
    	int randomNum;
    	int j;
    	j = 0;
    	int k;
    	k = 0;
    	int value;
    	while (j<24) {
        	randomNum = ThreadLocalRandom.current().nextInt(min, max + 1);
        	if (Collections.frequency(deck, randomNum) < 4) {
            	add = deck.add(randomNum);
            	j++;
        	}
    	}
   	 
    	//ASSIGNING CARDS TO PLAYERS AND DECKS
    	while(k<12) {
   		 value = deck.get(k);
   		 if (k%2==0) {
   			 add = playerMHand.add(value);
   		 } else {
   			 add = playerVHand.add(value);
   		 }
        	k++;
    	}
    	while(k<23) {
        	value = deck.get(k);
        	add = drawPile.add(value);
        	k++;
    	}
    	while(k<24) {
        	value = deck.get(k);
        	add = discardPile.add(value);
        	k++;
    	}
   	 
    	//OUTPUT OF ASSIGNING
    	System.out.println(deck);
    	System.out.println("Player M's hand: " + playerMHand);
    	System.out.println("Player V's hand: " + playerVHand);
    	System.out.println("Draw pile: " + drawPile);
    	System.out.println("Discard pile: " + discardPile);
   	 
    	//SCORING
   	 
    	int mScore = scoring(playerMHand);
    	System.out.println("M's hand is worth: " + mScore);
    	int vScore = scoring(playerVHand);
    	System.out.println("V's hand is worth: " + vScore);
   	 
    	//CATEGORIZING CARDS
    	List<Integer> lM = loner(playerMHand);
    	List<Integer> pM = pair(playerMHand);
    	List<Integer> tM = triplet(playerMHand);
        quadra(playerMHand, lM, tM);
   	 
    	System.out.println("The loners list for M is: "+ lM);
    	System.out.println("The pairs list for M is: "+ pM);
    	System.out.println("The triplets list for M is: "+ tM);
   	 
    	List<Integer> lV = loner(playerVHand);
    	List<Integer> pV = pair(playerVHand);
    	List<Integer> tV = triplet(playerVHand);
   	quadra(playerVHand, lV, tV);
        
    	System.out.println("The loners list for V is: "+ lV);
    	System.out.println("The pairs list for V is: "+ pV);
    	System.out.println("The triplets list for V is: "+ tV);
   	 
   	 
   	 
   	 
    	//PLAYING
        
        int done;
        done = 0;
        while (done == 0) {
            done = play(discardPile, drawPile, playerMHand, lM, pM, tM);
            System.out.println("After ONE MOVE BY M");
            System.out.println("Player M's hand: " + playerMHand);
            System.out.println("Draw pile: " + drawPile);
            System.out.println("Discard pile: " + discardPile);
            System.out.println("The loners list for M is: "+ lM);
            System.out.println("The pairs list for M is: "+ pM);
            System.out.println("The triplets list for M is: "+ tM);
            if (done == 0) {
                play(discardPile, drawPile, playerVHand, lV, pV, tV);
                System.out.println("After ONE MOVE BY V");
                System.out.println("Player V's hand: " + playerVHand);
                System.out.println("Draw pile: " + drawPile);
                System.out.println("Discard pile: " + discardPile);
                System.out.println("The loners list for V is: "+ lV);
                System.out.println("The pairs list for V is: "+ pV);
                System.out.println("The triplets list for V is: "+ tV);
            }
        }
  	 
    }
    
    public static int scoring(List<Integer> playerHand) {
   	 int c;
    	int sum;
   	 
    	sum = 0;
    	for(c = 0; c < playerHand.size(); c++) {
        	sum += playerHand.get(c);
    	}
   	 
    	int score;
    	score = sum;
   	 
    	int actualScore;
    	actualScore = score;
   	 
    	for(c = 1; c < 7; c++) {
        	if (Collections.frequency(playerHand, c) == 3) {
            	actualScore = actualScore - (3*c);
        	}
    	}
    	return actualScore;
    }
    
    public static List<Integer> loner(List<Integer> playerHand) {
   	 List<Integer> loners = new ArrayList<>();
    	int p;
    	int valueM;
    	for (p = 0; p < 6; p++) {
        	valueM = playerHand.get(p);
        	if (Collections.frequency(playerHand, valueM) == 1) {
            	if (loners.contains(valueM) == false) {
            	loners.add(valueM);
            	}
        	}
    	}
    	return loners;
    }
    public static List<Integer> pair(List<Integer> playerHand) {
   	 List<Integer> pairs = new ArrayList<>();
    	int p;
    	int valueM;
    	for (p = 0; p < 6; p++) {
        	valueM = playerHand.get(p);
        	if (Collections.frequency(playerHand, valueM) == 2) {
            	if (pairs.contains(valueM) == false) {
            	pairs.add(valueM);
            	}
        	}
    	}
    	return pairs;
    }
    public static List<Integer> triplet(List<Integer> playerHand) {
   	 List<Integer> triplets = new ArrayList<>();
    	int p;
    	int valueM;
    	for (p = 0; p < 6; p++) {
        	valueM = playerHand.get(p);
        	if (Collections.frequency(playerHand, valueM) == 3) {
            	if (triplets.contains(valueM) == false) {
           		 triplets.add(valueM);
            	}
        	}
    	}
    	return triplets;
    }
    public static void quadra(List<Integer> playerHand, List<Integer> loners, List<Integer> triplets) {
   	 List<Integer> quadra = new ArrayList<>();
    	int p;
    	int valueM;
    	for (p = 0; p < 6; p++) {
        	valueM = playerHand.get(p);
        	if (Collections.frequency(playerHand, valueM) == 4) {
            	if (triplets.contains(valueM) == false) {
                    if (loners.contains(valueM) == false) {
                        triplets.add(valueM);
                        loners.add(valueM);
                    }
            	}
        	}
    	}
    }
    
    public static int play(List<Integer> discard, List<Integer> draw, List<Integer> hand, List<Integer> loner, List<Integer> pair, List<Integer> triplet) {
   	int disTop;
    	disTop = discard.get(0);
    	int drawTop;
    	drawTop = draw.get(0);
    	int high;
        
        //check for winning condition
        if (pair.isEmpty() && loner.size() == 1) {
            discard.add(loner.get(0)); 
            hand.remove(hand.indexOf(loner.get(0)));
            return 1;
        }
        //winning condition is not met
        else {
            if (pair.contains(disTop)) {
   		 hand.add(disTop);
   		 triplet.add(disTop);
   		 pair.remove(pair.indexOf(disTop));
   		 discard.remove(discard.indexOf(disTop));
            }
   	 
            else {
                     hand.add(drawTop);
                     draw.remove(draw.indexOf(drawTop));
                     if (loner.contains(drawTop)) {
                             loner.remove(loner.indexOf(drawTop));
                             pair.add(drawTop);
                     } else if (pair.contains(drawTop)) {
                             pair.remove(pair.indexOf(drawTop));
                             triplet.add(drawTop);
                     } else if (triplet.contains(drawTop)) {        //what if you already have 3 cards of the same number
                             loner.add(drawTop);
                     } else {   			 //what happens when it is a totally new card
                             loner.add(drawTop);
                     }
            }
            if (!loner.isEmpty()) {
            high = Collections.max(loner);
            hand.remove(hand.indexOf(high));
            loner.remove(loner.indexOf(high));
            discard.add(0, high);
            }
            else if (!pair.isEmpty()) {
                high = Collections.max(pair);
                hand.remove(hand.indexOf(high));
                pair.remove(pair.indexOf(high));
                loner.add(high);
                discard.add(0, high);
            }
           return 0;
        }
        
    }
    
}
