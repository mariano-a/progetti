package stub;

public class StubAttrAssegnata {
	
	private StubAttrezzatura stubAttrezzatura;
	private StubBadge stubBadge;
	
	public StubAttrAssegnata(StubBadge stubBadge, StubAttrezzatura stubAttrezzatura) {
		super();
		this.stubBadge = stubBadge;
		this.stubAttrezzatura = stubAttrezzatura;
	}
	
	
	public StubBadge getBadge() {
		return stubBadge;
	}
	public void setBadge(StubBadge badge) {
		this.stubBadge = badge;
	}
	public StubAttrezzatura getAttrezzatura() {
		return stubAttrezzatura;
	}
	public void setAttrezzatura(StubAttrezzatura attrezzatura) {
		this.stubAttrezzatura = attrezzatura;
		
	}
}
