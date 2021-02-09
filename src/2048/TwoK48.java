// Direct translation from 2048.py

import java.io.*;
import java.util.*;

public class TwoK48 {
    public static void main(String[] args) throws IOException {
        InputStreamReader inp = new InputStreamReader(System.in);
        BufferedReader sc = new BufferedReader(inp);
        PrintWriter writer = new PrintWriter(System.out);
        
        List<List<Integer>> matrix = new ArrayList<List<Integer>>();
        for (int v = 0; v < 4; v ++) {
            List<Integer> row = new ArrayList<Integer>();
            String[] line = sc.readLine().split(" ");
            for (int vp = 0; vp < 4; vp++) {
                row.add(Integer.parseInt(line[vp]));
            }
            matrix.add(row);
        }

        int n = Integer.parseInt(sc.readLine());

        List<List<Integer>> answer;

        if (n == 0) {
            answer = mergeLeft(matrix);
        } else if (n == 1) {
            answer = mergeUp(matrix);
        } else if (n == 2) {
            answer = mergeRight(matrix);
        } else {
            answer = mergeDown(matrix);
        }

        for (int main1 = 0; main1 < 4; main1++) {
            for (int main2 = 0; main2 < 3; main2++) {
                writer.print(answer.get(main1).get(main2));
                writer.print(" ");
            }
            writer.println(answer.get(main1).get(3));
        }
        writer.flush();
    }

    public static List<Integer> flatten(List<List<Integer>> mat) {
        List<Integer> result = new ArrayList<Integer>();
        for (int f1 = 0; f1 < 4; f1++) {
            for (int f2 = 0; f2 < 4; f2++) {
                result.add(mat.get(f1).get(f2));
            }
        }
        return result;
    }

    public static List<List<Integer>> transpose(List<List<Integer>> mat) {
        List<List<Integer>> result = new ArrayList<List<Integer>>();
        for (int t1 = 0; t1 < 4; t1++) {
            List<Integer> row = new ArrayList<Integer>();
            for (int t2 = 0; t2 < 4; t2++) {
                row.add(mat.get(t2).get(t1));
            }
            result.add(row);
        }
        return result;
    }

    public static List<List<Integer>> reverse(List<List<Integer>> mat) {
        List<List<Integer>> result = new ArrayList<List<Integer>>();
        for (int r1 = 0; r1 < 4; r1++) {
            List<Integer> row = new ArrayList<Integer>();
            for (int r2 = 0; r2 < 4; r2++) {
                row.add(mat.get(r1).get(3-r2));
            }
            result.add(row);
        }
        return result;
    }

    public static List<List<Integer>> mergeLeft(List<List<Integer>> mat) {
        List<List<Integer>> newMatrix = new ArrayList<List<Integer>>();
        for (int ml1 = 0; ml1 < 4; ml1++) {
            newMatrix.add(mergifyLeftify(mat.get(ml1)));
        }
        return newMatrix;
    }

    public static List<Integer> mergifyLeftify(List<Integer> row) {
        int currIndex = 0;
        while (currIndex < row.size() && row.get(currIndex) == 0) {
            currIndex += 1;
        }
        int nextIndex = currIndex + 1;
        while (nextIndex < row.size() && row.get(nextIndex) == 0) {
            nextIndex += 1;
        }

        if (nextIndex == row.size()) {
            row.set(0, row.get(currIndex));
            if (currIndex != 0) {
                row.set(currIndex, 0);
            }
            return row;
        } else if (currIndex == row.size()) {
            return row;
        } else {
            if (row.get(currIndex).equals(row.get(nextIndex))) {
                row.set(currIndex,row.get(currIndex)*2);
                row.set(nextIndex,0);
                int t = row.get(currIndex);

                List<Integer> newRow = new ArrayList<Integer>();
                List<Integer> subRow = row.subList(nextIndex+1,row.size());
                newRow.add(t);
                for (int repZero1 = 0; repZero1 < nextIndex; repZero1++) {
                    subRow.add(0);
                }
                List <Integer> nextMerge = mergifyLeftify(subRow);
                for (int nm1 = 0; nm1 < nextMerge.size(); nm1++) {
                    newRow.add(nextMerge.get(nm1));
                }
                return newRow;
            } else {
                if (currIndex != nextIndex-1) {
                    row.set(currIndex+1,row.get(nextIndex));
                    row.set(nextIndex,0);
                    nextIndex = currIndex + 1;
                }
                int t = row.get(currIndex);

                List<Integer> newRow = new ArrayList<Integer>();
                List<Integer> subRow = row.subList(nextIndex,row.size());
                newRow.add(t);
                for (int repZero2 = 0; repZero2 < currIndex; repZero2++) {
                    subRow.add(0);
                }
                List <Integer> nextMerge = mergifyLeftify(subRow);
                for (int nm2 = 0; nm2 < nextMerge.size(); nm2++) {
                    newRow.add(nextMerge.get(nm2));
                }
                return newRow;
            }
        }
    }

    public static List<List<Integer>> mergeRight(List<List<Integer>> mat) {
        List<List<Integer>> mState = mergeLeft(reverse(mat));
        return reverse(mState);
    }

    public static List<List<Integer>> mergeUp(List<List<Integer>> mat) {
        List<List<Integer>> mState = mergeLeft(transpose(mat));
        return transpose(mState);
    }

    public static List<List<Integer>> mergeDown(List<List<Integer>> mat) {
        List<List<Integer>> mState = mergeRight(transpose(mat));
        return transpose(mState);
    }
}