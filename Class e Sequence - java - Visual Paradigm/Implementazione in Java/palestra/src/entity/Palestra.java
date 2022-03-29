package entity;

import java.util.ArrayList;

import stub.*;

public class Palestra {
	
	private ArrayList<Socio> aSocio;
	private ArrayList<Attrezzatura> aAttrezzatura;
	private ArrayList<Badge> aBadge;
	private ArrayList<Accesso> aAccesso;
	private ArrayList<AttrAssegnata> aAttrAssegnata;
	
	public Palestra(){
		System.out.println("Costruttore palestra inizio");
		StubPalestra sPalestra = new StubPalestra();
		System.out.println("Costruttore palestra dopo stubpalestra");
		aSocio = new ArrayList<Socio>();
		aAttrezzatura= new ArrayList<Attrezzatura>();
		aBadge = new ArrayList<Badge>();
		aAccesso = new ArrayList<Accesso>();
		aAttrAssegnata = new ArrayList<AttrAssegnata>();
		Attrezzatura attrezzatura = new Attrezzatura();
		Socio socio = new Socio();
		Badge badge= new Badge();
		Accesso accesso = new Accesso();
		
		
		System.out.println("Costruttore palestra dopo stubpalestra 1");
		//ATTREZZATURA 
		int sizeAttr = sPalestra.getaStubAttrezzatura().size();
		for(int i = 0; i < sizeAttr; i++) {
			attrezzatura.setId_attr(sPalestra.getaStubAttrezzatura().get(i).getId_attr());
			attrezzatura.setTipo(sPalestra.getaStubAttrezzatura().get(i).getTipo());
			aAttrezzatura.add(attrezzatura);
		}
		
		System.out.println("Costruttore palestra dopo stubpalestra 3");
		//SOCI
		int sizes = sPalestra.getaStubSocio().size();
		for(int i = 0; i < sizes; i++) {
			socio.setNome(sPalestra.getaStubSocio().get(i).getNome());
			socio.setCognome(sPalestra.getaStubSocio().get(i).getCognome());
			socio.setData_nascita(sPalestra.getaStubSocio().get(i).getData_nascita());
			aSocio.add(socio);
		}
		System.out.println("Costruttore palestra dopo stubpalestra 4");
		//BADGE
		int sizeBadge = sPalestra.getaStubBadge().size();
		for(int i=0; i < sizeBadge; i++) {
			badge.setId_badge(sPalestra.getaStubBadge().get(i).getId_badge());
			aBadge.add(badge);
			System.out.println(badge.getId_badge());
			
		}
		System.out.println("Costruttore palestra dopo stubpalestra 5");
		//ACCESSI
		int sizeAccesso = sPalestra.getaStubAccesso().size();
		for(int i=0; i<sizeAccesso;i++) {
			accesso.setId_badge(sPalestra.getaStubAccesso().get(i).getId_badge());
			accesso.setData(sPalestra.getaStubAccesso().get(i).getData());
			accesso.setOra(sPalestra.getaStubAccesso().get(i).getOra());
			aAccesso.add(accesso);
		}
		System.out.println("Costruttore palestra dopo stubpalestra 6");
//		//ATTREZZATURE ASSEGNATE AI SOCI	
		System.out.println(aBadge.get(0));
		
		AttrAssegnata assegnata1 = new AttrAssegnata(aBadge.get(0),aAttrezzatura.get(0));
		AttrAssegnata assegnata2 = new AttrAssegnata(aBadge.get(1),aAttrezzatura.get(1));
		
		
		aAttrAssegnata.add(assegnata1);
		aAttrAssegnata.add(assegnata2);
		
	
		
		
		System.out.println("Costruttore palestra fine");
		
	}
	
	
	public Badge verificaBadge(int id_badge) {
		System.out.println("verificaBadge");
		for(int i=0; i < aBadge.size(); i++) {
			if(id_badge == aBadge.get(i).getId_badge()) {
				
				return aBadge.get(i);
			}
			System.out.println(aBadge.get(i).getId_badge());
		}
		System.out.println("a");
		return null;
	}
	
	public Accesso verificaAccesso(int id_badge) {
		System.out.println("verificaAccesso");
		for(int i=0; i < aAccesso.size(); i++) {
			if(id_badge == aAccesso.get(i).getId_badge()) {
				return aAccesso.get(i);
			}
		}
		
		return null;
	}
	
	public AttrAssegnata verificaUtilizzoAttr(int id_badge) {
		System.out.println("verificaUtilizzoAttr");
		for(int i=0; i < aAttrAssegnata.size(); i++) {
			if(id_badge != aAttrAssegnata.get(i).getBadge().getId_badge()) {
				return aAttrAssegnata.get(i);
			}
		}
		return null;
	}
	
	public Attrezzatura cercaAttrezzaturaDisp(String tipo) {
		System.out.println("cercaAttrezzaturaDisp");
		for(int i=0; i < aAttrezzatura.size(); i++) {
				if(tipo.equals(aAttrezzatura.get(i).getTipo()))
				{
					for(int j=0; j < aAttrAssegnata.size(); j++)
					{
						if(aAttrezzatura.get(i).getId_attr() == aAttrAssegnata.get(i).getAttrezzatura().getId_attr())	break;
					}
					
					return aAttrezzatura.get(i);
				}

			}
		return null;
	}
	
	public int assegnaAttrezzatura(Attrezzatura attrezzatura, Badge badge) {
		System.out.println("assegnaAttrezzatura");
		AttrAssegnata assegnazione = new AttrAssegnata();
		assegnazione.setBadge(badge);
		assegnazione.setAttrezzatura(attrezzatura);
		return attrezzatura.getId_attr();
		
	} 
	
	public void depositaAttrezzatura(int id_badge) {
		for(int i=0; i < aAttrAssegnata.size(); i++) {
			if(id_badge == aAttrAssegnata.get(i).getBadge().getId_badge()) {
				aAttrAssegnata.remove(aAttrAssegnata.get(i));
			}
		}
		
	}
	
}
