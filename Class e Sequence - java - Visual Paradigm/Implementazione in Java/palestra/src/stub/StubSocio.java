package stub;


public class StubSocio {

	private String nome;
	private String cognome;
	private String data_nascita;
	private StubBadge stubBadge;
	
	
	public String getData_nascita() {
		return data_nascita;
	}
	public void setData_nascita(String data_nascita) {
		this.data_nascita = data_nascita;
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
	
	public StubBadge getBadge() {
		return stubBadge;
	}
	public void setBadge(StubBadge stubBadge) {
		this.stubBadge = stubBadge;
	}
	
	public StubSocio(String nome, String cognome, String data_nascita, StubBadge stubBadge) {
		super();
		this.nome = nome;
		this.cognome = cognome;
		this.data_nascita = data_nascita;
		this.stubBadge = stubBadge;
		
	}
	
}
