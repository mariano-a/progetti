package controller;

import entity.*;

public class Controller {

	private Palestra palestra;
	

	public Controller() {
		this.setPalestra(new Palestra());
		System.out.println("Costruttore controller");
		
	}
	
	
	public int RichiestaAttrezzatura(int id_badge, String tipo) {
		
		Badge badge = palestra.verificaBadge(id_badge);
		if(badge == null) return -1;
		Accesso accesso = palestra.verificaAccesso(id_badge);
		if(accesso == null) 	return -2;
		AttrAssegnata assegnazione = palestra.verificaUtilizzoAttr(id_badge);
		if(assegnazione == null)	return -3;
		
		Attrezzatura attrezzatura= palestra.cercaAttrezzaturaDisp(tipo);
		return palestra.assegnaAttrezzatura(attrezzatura,badge);
	}
	
	public boolean UscitaPalestra(int id_badge) {
		AttrAssegnata assegnazione = palestra.verificaUtilizzoAttr(id_badge);
		if(assegnazione == null)	return false;
		palestra.depositaAttrezzatura(id_badge);
		return true;
	}
	
	public Palestra getPalestra() {
		return palestra;
	}


	public void setPalestra(Palestra palestra) {
		this.palestra = palestra;
	}
	
	
	
}
