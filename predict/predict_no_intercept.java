import java.lang.Math;
class predict_no_intercept
{
    public static void main(String args[])
    {
        //Parameter definition
        int numPoses = 4;
        //Define the features array
        double Features[];
        //Declare the features array
        //Features = new double[8];
        //Define trial set of Features (Boat chosen for reference)
        Features = new double[]{43.34667507d,47.05595858d,43.34667507d,142.3389672d,168.0415926d,10.46603823d,54.8243765d,42.78103997d};
        //Define trial set of Features (Bow chosen for reference)
        //Features = new double[]{100.7468022d,107.9266013d,100.7468022d,169.8138723d,100.5559779d,84.52468342d,82.83820404d,89.41130784d};
        //Define trial set of Features (Camel chosen for reference)
        //Features = new double[]{87.72488059d,86.66112663d,87.72488059d,42.48518198d,127.4737749d,45.648273d,49.07353835d,47.22077994d};
        //Define trial set of Features (Cat chosen for reference)
        //Features = new double[]{74.13640285d,100.0295803d,74.13640285d,177.4309618d,139.3307355d,40.2247394d,99.72238489d,96.90069472d};
        //Define the beta array
        double beta[][];
        //Declare beta for 4 poses with 8 features each (no value for intercept)
        beta = new double[numPoses][8];
        //Manually input data from csv
        double beta_boat[];
        double beta_bow[];
        double beta_camel[];
        double beta_cat[];
        beta_boat = new double[]{-0.024446798d,0.010530453d,-0.024446798d,0.035196611d,0.028304167d,-0.038208047d,0.021196301d,-0.050576457d};
        beta_bow = new double[]{-0.007448579d,0.018768332d,-0.007448579d,0.046137089d,-0.034538625d,0.003081071d,0.01282512d,-0.025040231d};       
        beta_camel = new double[]{-0.003415977d,0.019153244d,-0.003415977d,0.030297826d,-0.012425267d,-0.002342858d,0.003850182d,-0.034207269d};
        beta_cat = new double[]{-0.00474824d,-0.006936133d,-0.00474824d,0.076988958d,-0.036352846d,-0.034145395d,0.041731144d,-0.056597111d};
        //Densify the beta matrix
        
        for(int i = 0;i<=beta_boat.length-1;i++) //traversing the weights
        {
            beta[0][i] = beta_boat[i];
            beta[1][i] = beta_bow[i];
            beta[2][i] = beta_camel[i];
            beta[3][i] = beta_cat[i];

        }
      
        //Calculating y value
        double y[];
        y= new double[numPoses+1];
        //Add the 0 intercepts
        /*
        y[0] = beta[0][0];
        y[1] = beta[1][0];
        y[2] = beta[2][0];
        y[3] = beta[3][0];
        */
        //Multiply features and add
        for (int i= 0;i<=beta_boat.length-1;i++)
        {
                y[0] += beta[0][i]*Features[i];
                y[1] += beta[1][i]*Features[i];
                y[2] += beta[2][i]*Features[i];
                y[3] += beta[3][i]*Features[i];
        }

        
        double z[]=new double[]{y[0],y[1],y[2],y[3]};
        double nume[]=new double[]{0.0d,0.0d,0.0d,0.0d};
        double Denom = 0.0d;
        double softmax[]=new double[]{0.0d,0.0d,0.0d,0.0d};
        for (int i =0;i<=numPoses-1;i++)
        {
            nume[i] = Math.exp(z[i]);
            Denom += Math.exp(z[i]);
            

        }
        for (int i =0;i<=numPoses-1;i++)
        {
            softmax[i] = nume[i]/Denom;
            System.out.println(softmax[i]);
        }
        int max_i = 0;
        double max_softmax = softmax[0];
        for(int i = 1; i<=numPoses-1;i++)
        {
            if(softmax[i]>max_softmax)
            {
                max_softmax = softmax[i];
                max_i = i;
            }
            
        }

        String pose_name = "";
        switch(max_i+1)
        {
            case 1: pose_name = "boat";
            break;
            case 2: pose_name = "bow";
            break;
            case 3: pose_name = "camel";
            break;
            case 4: pose_name = "cat";
            break;
            default: pose_name = "Not Found";
            break;
        }
        System.out.println(pose_name);
    }

}