interface axe{
	void display();
}
class a5 implements axe{
	final int num=9;
	public void add(){
		System.out.println(num);
	}
	public void display(){
		System.out.println(num);
	}

	public static void main(String args[])
	{
		a5 obj=new a5();
		obj.add();
		obj.display();
	}
}