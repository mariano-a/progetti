package entity;


public class AttrAssegnata {
	private Attrezzatura attrezzatura;
	private Badge badge;
	
	public AttrAssegnata(Badge badge, Attrezzatura attrezzatura) {
	
		this.badge = badge;
		this.attrezzatura = attrezzatura;
		
	}
	
	public AttrAssegnata() {}
	
	
	public Badge getBadge() {
		return badge;
	}
	public void setBadge(Badge badge) {
		this.badge = badge;
	}
	public Attrezzatura getAttrezzatura() {
		return attrezzatura;
	}
	public void setAttrezzatura(Attrezzatura attrezzatura) {
		this.attrezzatura = attrezzatura;
		
	}
	
}
