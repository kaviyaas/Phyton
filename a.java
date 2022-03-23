class student{
	public int custid;
	student(int custid){
		custid=custid;
		System.out.println(custid);
	}
	student(){
		System.out.println("hlo");
	}
}
class a{
	public static void main(String args[]){
		student s=new student();
		new student(234);
	}
}