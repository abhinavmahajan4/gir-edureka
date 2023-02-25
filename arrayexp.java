import java.util.Arrays;
public class arrayexp{
	public static void main (String args[]){
		
		int[] marks= new int[4];
		// int j;
		int i=0;
		int phy=90;
		int chem=86;
		int bio=100;
		int math=98;
		marks[0]=phy;
		marks[1]=chem;
		marks[2]=math;
		marks[3]=bio;
		// System.out.println(j);
		for (i=0;i<=3;i++){
		System.out.println(marks[i]);
		
		}
		Arrays.sort(marks);
		for (i=0;i<=3;i++){
		System.out.println(marks[i]);
		
		}
		
	
	
	}

}