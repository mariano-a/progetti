package entity;


public class Socio {

	private String nome;
	private String cognome;
	private String data_nascita;
	private Badge badge;
	

	public Socio() {}
	
	public Socio(String nome, String cognome, String data_nascita, Badge badge) {
		super();
		this.nome = nome;
		this.cognome = cognome;
		this.data_nascita = data_nascita;
		this.badge = badge;
	}
	
	public String getNome() {
		return nome;
	}

	public void setNome(String nome) {
		this.nome = nome;
	}

	public String getCognome() {
		return cognome;
	}

	public void setCognome(String cognome) {
		this.cognome = cognome;
	}

	public String getData_nascita() {
		return data_nascita;
	}
	
	public void setData_nascita(String data_nascita) {
		this.data_nascita = data_nascita;
	}
	
	public Badge getBadge() {
		return badge;
	}

	public void setBadge(Badge badge) {
		this.badge = badge;
	}
}
