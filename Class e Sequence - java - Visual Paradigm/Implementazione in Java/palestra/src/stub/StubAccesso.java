package stub;

public class StubAccesso {
	private int id_badge;
	private String data;
	private String ora;
	
	public int getId_badge() {
		return id_badge;
	}
	public void setId_badge(int id_badge) {
		this.id_badge = id_badge;
	}
	public String getData() {
		return data;
	}
	public void setData(String data) {
		this.data = data;
	}
	public String getOra() {
		return ora;
	}
	public void setOra(String ora) {
		this.ora = ora;
	}
	
	public StubAccesso(int id_badge, String data, String ora) {
		super();
		this.id_badge = id_badge;
		this.data = data;
		this.ora= ora;
	}
}
