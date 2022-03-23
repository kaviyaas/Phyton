class bike{
	int speed=40;
}
class honda extends bike{
	int speed=56;
	
}
class peps extends bike{
	int speed=89;
	{
		
	}
}
class b7{
 public static void main(String args[]){
	bike b1=new bike();
	honda h1=new honda();
	peps p1=new peps();
	bike b2=new peps();
	System.out.println(b1.speed);
	System.out.println(h1.speed);
	System.out.println(p1.speed);
	System.out.println(b2);
	}
}
 