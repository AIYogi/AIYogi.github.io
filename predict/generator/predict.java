import java.lang.Math;
class predict
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
        //Features = new double[]{43.34667507d,47.05595858d,43.34667507d,142.3389672d,168.0415926d,10.46603823d,54.8243765d,42.78103997d};
        //Features = new double[]{95.49323809d,102.5213561d,95.49323809d,171.0429973d,145.0943978d,44.81397857d,86.54435774d,82.62301088d};
        Features = new double[]{103.6056157d,99.14506108d,103.6056157d,178.2715656d,108.6437535d,80.75782959d,91.52069092d,94.01970903d};
        //Define the beta array
        double beta[][];
        //Declare beta for 4 poses with 8 features each (0th value for intercept)
        beta = new double[numPoses][9];
        //Manually input data from csv
        double beta_boat[];
        double beta_bow[];
        double beta_camel[];
        double beta_cat[];
        beta_boat = new double[]{0.676172954d,-0.024446798d,0.010530453d,-0.024446798d,0.035196611d,0.028304167d,-0.038208047d,0.021196301d,-0.050576457d};
        beta_bow = new double[]{-0.075702333d,-0.007448579d,0.018768332d,-0.007448579d,0.046137089d,-0.034538625d,0.003081071d,0.01282512d,-0.025040231d};       
        beta_camel = new double[]{0.462547791d,-0.003415977d,0.019153244d,-0.003415977d,0.030297826d,-0.012425267d,-0.002342858d,0.003850182d,-0.034207269d};
        beta_cat = new double[]{-0.1212961d,-0.00474824d,-0.006936133d,-0.00474824d,0.076988958d,-0.036352846d,-0.034145395d,0.041731144d,-0.056597111d};
        //Densify the beta matrix
        for(int i = 0;i<=numPoses-1;i++) //traversing the poses
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
        y[0] = beta[0][0];
        y[1] = beta[1][0];
        y[2] = beta[2][0];
        y[3] = beta[3][0];
        //Multiply features and add
        for (int i= 1;i<=8;i++)
        {
                y[0] += beta[0][i]*Features[i-1];
                y[1] += beta[1][i]*Features[i-1];
                y[2] += beta[2][i]*Features[i-1];
                y[3] += beta[3][i]*Features[i-1];
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
        for(int i = 0; i<=numPoses-1;i++)
        {
            if(softmax[i]>max_softmax)
            {
                max_i = i;
            }
            
        }

        String pose_name = "";
        System.out.println(max_i);
        switch(max_i)
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


        
/*
        double a1 = Math.exp(y[0]);
        double a2 = Math.exp(y[1]);
        double a3 = Math.exp(y[2]);
        double a4 = Math.exp(y[3]);
        double sum = Math.exp(y[0]+y[1]+y[2]+y[3]);
        double p1 = a1/sum;//(a1+a2+a3+a4);
        double p2 = a2/sum;//(a1+a2+a3+a4);
        double p3 = a3/sum;//(a1+a2+a3+a4);
        double p4 = a4/sum;//(a1+a2+a3+a4);
        System.out.println(a1);
        System.out.println(p1);
        System.out.println(a2);
        System.out.println(p2);


        //Calculating probabilities
        double p[];
        p = new double[numPoses];

        double sum_p = 0.0d;
        for (int i= 0;i<=numPoses-1;i++)
        {
                p[i] = sigmoidFunction(y[i]);
                //System.out.println(p[i]);
                sum_p += p[i];
        }
        //Find maximum probability
        
        double max_p = p[0]/sum_p;
        for(int i = 0; i<=numPoses-1;i++)
        {
            if((p[i]/sum_p)>max_p)
            {
                max_p = (p[i]/sum_p);
            }
            
        }
        int search_p= (int)(Math.round(max_p));
        String pose_name = "";
        //System.out.println(search_p);
        switch(search_p)
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
        //System.out.println(pose_name);

     */       

    }
    public static double sigmoidFunction(double a)
    {
        double val = 1/(1+Math.exp(a));
        return val;
    }

}