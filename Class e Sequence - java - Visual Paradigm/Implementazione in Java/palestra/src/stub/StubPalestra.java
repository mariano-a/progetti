package stub;

import java.util.ArrayList;
	
public class StubPalestra {
	
	private ArrayList<StubSocio> aStubSocio;
	private ArrayList<StubAttrezzatura> aStubAttrezzatura;
	private ArrayList<StubBadge> aStubBadge;
	private ArrayList<StubAccesso> aStubAccesso;
	private ArrayList<StubAttrAssegnata> aStubAttrAssegnata;
	

	public StubPalestra() {
		System.out.println("Costruttore stubpalestra inizio");
		this.aStubSocio = new ArrayList<StubSocio>();
		this.aStubAttrezzatura = new ArrayList<StubAttrezzatura>();
		this.aStubBadge = new ArrayList<StubBadge>();
		this.aStubAccesso = new ArrayList<StubAccesso>();
		this.aStubAttrAssegnata = new ArrayList<StubAttrAssegnata>();
		
		// STUB BADGE //
		StubBadge badge=new StubBadge(0);
		StubBadge badge1=new StubBadge(1);
		StubBadge badge2=new StubBadge(2);
		StubBadge badge3=new StubBadge(3);
		
		aStubBadge.add(badge);
		aStubBadge.add(badge1);
		aStubBadge.add(badge2);
		aStubBadge.add(badge3);
		
		System.out.println("Costruttore stubpalestra badge");
		
		// STUB SOCIO //
		StubSocio socio = new StubSocio("Giovanni","Rossi","07/03/1998",badge);
		StubSocio socio1 = new StubSocio("Paolo","Verdi","05/10/1997",badge1);
		StubSocio socio2 = new StubSocio("Paolo","Giallo","05/10/1997",badge2);
		aStubSocio.add(socio);
		aStubSocio.add(socio1);
		aStubSocio.add(socio2);
		
		// STUB ATTREZZATURA //
		StubAttrezzatura attrezzatura= new StubAttrezzatura(0, "Tapis roulant");
		StubAttrezzatura attrezzatura1= new StubAttrezzatura(1, "Cyclette");
		StubAttrezzatura attrezzatura2= new StubAttrezzatura(2, "Vogatore");
		StubAttrezzatura attrezzatura3= new StubAttrezzatura(3, "Stepper");
		StubAttrezzatura attrezzatura4= new StubAttrezzatura(4, "Ellittica");
		
		aStubAttrezzatura.add(attrezzatura);
		aStubAttrezzatura.add(attrezzatura3);
		aStubAttrezzatura.add(attrezzatura1);
		aStubAttrezzatura.add(attrezzatura2);
		aStubAttrezzatura.add(attrezzatura4);
		
		System.out.println("Costruttore stubpalestra attrezzatura");
		
		
		System.out.println("Costruttore stubpalestra accesso");
		
		StubAccesso accesso= new StubAccesso(0,"13/01/2020","13.40");
		StubAccesso accesso1= new StubAccesso(0,"13/01/2020","19.30");
		StubAccesso accesso2= new StubAccesso(0,"13/01/2020","15.00");
	
		aStubAccesso.add(accesso);
		aStubAccesso.add(accesso1);
		aStubAccesso.add(accesso2);
		

		System.out.println("Costruttore stubpalestra fine");
	}
	
	public ArrayList<StubSocio> getaStubSocio(){
		return aStubSocio;
	}
	
	public void setaStubSocio(ArrayList<StubSocio> aStubSocio) {
		this.aStubSocio = aStubSocio;
	}
	
	public ArrayList<StubBadge> getaStubBadge(){
		return aStubBadge;
	}
	public void setaStubBadge(ArrayList<StubBadge> aStubBadge) {
		this.aStubBadge = aStubBadge;
	}
	
	public ArrayList<StubAccesso> getaStubAccesso(){
		return aStubAccesso;
	}
	public void setaStubAccesso(ArrayList<StubAccesso> aStubAccesso) {
		this.aStubAccesso = aStubAccesso;
	}
	
	public ArrayList<StubAttrAssegnata> getaStubAttrAssegnata() {
		return aStubAttrAssegnata;
	}
	public void setaStubAttrAssegnata(ArrayList<StubAttrAssegnata> aStubAttrAssegnata) {
		this.aStubAttrAssegnata = aStubAttrAssegnata;
	}

	public ArrayList<StubAttrezzatura> getaStubAttrezzatura() {
		return aStubAttrezzatura;
	}

	public void setaStubAttrezzatura(ArrayList<StubAttrezzatura> aStubAttrezzatura) {
		this.aStubAttrezzatura = aStubAttrezzatura;
	}
}
