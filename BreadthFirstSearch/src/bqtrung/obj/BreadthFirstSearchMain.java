package bqtrung.obj;

import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;
import java.util.Map;
import java.util.stream.Collectors;

public class BreadthFirstSearchMain {

	@SuppressWarnings("unchecked")
	public ArrayList<Integer> BFS(int s, int g, ArrayList<Integer> list) {
		@SuppressWarnings("rawtypes")
		Map<Integer, Boolean> hm = new HashMap();

		List<Integer> listWithoutDuplicates = list.stream().distinct().collect(Collectors.toList());

		for (int i = 0; i < listWithoutDuplicates.size(); i++) {
			hm.put(listWithoutDuplicates.get(i), false);
		}

		ArrayList<Integer> open = new ArrayList<Integer>();

		ArrayList<Integer> close = new ArrayList<Integer>();

		open.add(s);

		int p = 0;
		int temp = 0;
		while (open.size() > 0) {
			p = open.get(0);

			open.remove(0);

			hm.put(p, true);

			for (int i = 0; i < list.size() - 1; i++) {
				if (list.get(i) == p && hm.get(list.get(i + 1)) == false) {
					open.add(list.get(i + 1));
				}
			}
			close.add(p);
			if (p == g) {
				temp = 1;
				break;
			}

		}
		if (temp == 1) {
			return close;
		}
		return null;
	}

	public static void main(String args[]) {
		BreadthFirstSearchMain abc = new BreadthFirstSearchMain();
		ArrayList<Integer> ab = new ArrayList<Integer>();
		ab.add(0);
		ab.add(1);
		ab.add(0);
		ab.add(2);
		ab.add(0);
		ab.add(3);
		ab.add(2);
		ab.add(4);
		
		
		ArrayList<Integer> a = abc.BFS(0, 4, ab);
			
		System.out.print(a);
	}
}
