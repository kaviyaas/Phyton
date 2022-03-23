class a{
	public void add(int a,int b){
		int res=a+b;
		System.out.println(res);
	}
	public void add(){
		int a=23;
		int b=34;
		int res=a+b;
		System.out.println(res);
	}
	public void add(int a ,float b){
		float res=a+b;
		System.out.println(res);
	}
}
class b1{
	public static void main(String args[]){
		a a1=new a();
		a1.add(2,3);
		a1.add();
		a1.add(2,7.8f);
	}
}

		