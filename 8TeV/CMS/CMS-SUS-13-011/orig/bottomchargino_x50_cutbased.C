{

  TFile* f = TFile::Open("bottomchargino_x50_cutbased.root");

  TCanvas *c1 = new TCanvas("c1","",800,600);
  c1->cd();
  gPad->SetLogz();
  gPad->SetRightMargin(0.2);

  xsec_upperlimit->GetYaxis()->SetRangeUser(0,400);
  xsec_upperlimit->Draw("colz");
  observed_exclusion->Draw("cont3same");
  expected_exclusion->Draw("cont3same");

}
