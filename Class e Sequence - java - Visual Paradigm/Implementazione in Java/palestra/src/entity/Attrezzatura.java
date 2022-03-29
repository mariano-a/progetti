package entity;

public class Attrezzatura {
	private int id_attr;
	private String tipo;
	
	public int getId_attr() {
		return id_attr;
	}
	public String getTipo() {
		return tipo;
	}
	public void setId_attr(int id_attr) {
		this.id_attr=id_attr;
	}
	public void setTipo(String tipo) {
		this.tipo = tipo;
	}
	
	public Attrezzatura(int id_attr, String tipo) {
		super();
		this.id_attr =id_attr;
		this.tipo=tipo;
	}
	
	public Attrezzatura() {}
}
