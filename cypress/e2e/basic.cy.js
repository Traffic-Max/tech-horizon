describe('empty spec', () => {
  beforeEach(() => {
    cy.visit('/');
  });
  it('checks for the presence of an h2 header', () => {
    cy.get('h2').should('exist');
  });
  it('renders the image', () => {
    cy.get('img')
      .should('be.visible')
      .and(($img) => {
        expect($img[0].naturalWidth).to.be.greaterThan(0);
      });
  });
});
