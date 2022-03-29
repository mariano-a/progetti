package entity;

public class Badge {
	private int id_badge;
	
	public int getId_badge() {
		return id_badge;
	}
	
	public void setId_badge(int id_badge) {
		this.id_badge= id_badge;
	}
	
	public Badge(int id_badge) {
		super();
		this.id_badge = id_badge;
	}
	
	public Badge() {}
}
