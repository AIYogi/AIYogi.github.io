package com.google.mlkit.vision.demo.java.posedetector;

import android.graphics.Canvas;
import android.graphics.Color;
import android.graphics.Paint;
import android.graphics.PointF;
import android.graphics.RectF;
import android.util.Log;
import androidx.annotation.Nullable;
import com.google.mlkit.vision.demo.
        GraphicOverlay;
import com.google.mlkit.vision.demo.GraphicOverlay.Graphic;
import com.google.mlkit.vision.pose.Pose;
import com.google.mlkit.vision.pose.PoseLandmark;
import java.util.List;
import java.util.Locale;



/** Draw the detected pose in preview. */
public class PoseGraphic extends Graphic {

  private static final float DOT_RADIUS = 8.0f;
  private static final float IN_FRAME_LIKELIHOOD_TEXT_SIZE = 30.0f;
  private final Pose pose;
  private final boolean showInFrameLikelihood;
  private final Paint leftPaint;
  private final Paint rightPaint;
  private final Paint whitePaint;

  PoseGraphic(GraphicOverlay overlay, Pose pose, boolean showInFrameLikelihood) {
    super(overlay);

    this.pose = pose;
    this.showInFrameLikelihood = showInFrameLikelihood;

    whitePaint = new Paint();
    whitePaint.setColor(Color.WHITE);
    whitePaint.setTextSize(IN_FRAME_LIKELIHOOD_TEXT_SIZE);
    leftPaint = new Paint();
    leftPaint.setColor(Color.GREEN
    );
    rightPaint = new Paint();
    rightPaint.setColor(Color.YELLOW);
  }

  @Override
  public void draw(Canvas canvas) {
    List<PoseLandmark> landmarks = pose.getAllPoseLandmarks();
    if (landmarks.isEmpty()) {
      return;
    }
    // Draw all the points
    for (PoseLandmark landmark : landmarks) {
      drawPoint(canvas, landmark.getPosition(), whitePaint);
      if (showInFrameLikelihood) {
        canvas.drawText(
                String.format(Locale.US, "%.2f", landmark.getInFrameLikelihood(
                )),
                translateX(landmark.getPosition().x),
                translateY(landmark.getPosition().y),
                whitePaint);
      }
    }
    PoseLandmark leftShoulder = pose.getPoseLandmark(
            PoseLandmark.LEFT_SHOULDER);
    PoseLandmark rightShoulder = pose.getPoseLandmark(PoseLandmark.RIGHT_SHOULDER);
    PoseLandmark leftElbow = pose.getPoseLandmark(PoseLandmark.LEFT_ELBOW);
    PoseLandmark rightElbow = pose.getPoseLandmark(PoseLandmark.RIGHT_ELBOW);
    PoseLandmark leftWrist = pose.getPoseLandmark(PoseLandmark.LEFT_WRIST);
    PoseLandmark rightWrist = pose.getPoseLandmark(PoseLandmark.RIGHT_WRIST);
    PoseLandmark leftHip = pose.getPoseLandmark(PoseLandmark.LEFT_HIP);
    PoseLandmark rightHip = pose.getPoseLandmark(PoseLandmark.RIGHT_HIP);
    PoseLandmark leftKnee = pose.getPoseLandmark(PoseLandmark.LEFT_KNEE);
    PoseLandmark rightKnee = pose.getPoseLandmark(PoseLandmark.RIGHT_KNEE);
    PoseLandmark leftAnkle = pose.getPoseLandmark(PoseLandmark.LEFT_ANKLE);
    PoseLandmark rightAnkle = pose.getPoseLandmark(PoseLandmark.RIGHT_ANKLE);

    PoseLandmark leftPinky = pose.getPoseLandmark(PoseLandmark.LEFT_PINKY);
    PoseLandmark rightPinky = pose.getPoseLandmark(PoseLandmark.RIGHT_PINKY);
    PoseLandmark leftIndex = pose.getPoseLandmark(PoseLandmark.LEFT_INDEX);
    PoseLandmark rightIndex = pose.getPoseLandmark(PoseLandmark.RIGHT_INDEX);
    PoseLandmark leftThumb = pose.getPoseLandmark(PoseLandmark.LEFT_THUMB);
    PoseLandmark rightThumb = pose.getPoseLandmark(PoseLandmark.RIGHT_THUMB);
    PoseLandmark leftHeel = pose.getPoseLandmark(PoseLandmark.LEFT_HEEL);
    PoseLandmark rightHeel = pose.getPoseLandmark(PoseLandmark.RIGHT_HEEL);
    PoseLandmark leftFootIndex = pose.getPoseLandmark(PoseLandmark.LEFT_FOOT_INDEX);
    PoseLandmark rightFootIndex = pose.getPoseLandmark(PoseLandmark.RIGHT_FOOT_INDEX);
    double righthip = getAngle(
            pose.getPoseLandmark(PoseLandmark.RIGHT_SHOULDER),
            pose.getPoseLandmark(PoseLandmark.RIGHT_HIP),
            pose.getPoseLandmark(PoseLandmark.RIGHT_KNEE));
    double rightknee = getAngle(
            pose.getPoseLandmark(PoseLandmark.RIGHT_HIP),
            pose.getPoseLandmark(PoseLandmark.RIGHT_KNEE),
            pose.getPoseLandmark(PoseLandmark.RIGHT_ANKLE));
    double leftknee = getAngle(
            pose.getPoseLandmark(PoseLandmark.LEFT_HIP),
            pose.getPoseLandmark(PoseLandmark.LEFT_KNEE),
            pose.getPoseLandmark(PoseLandmark.LEFT_ANKLE));
    double leftelbow = getAngle(
            pose.getPoseLandmark(PoseLandmark.LEFT_SHOULDER),
            pose.getPoseLandmark(PoseLandmark.LEFT_ELBOW),
            pose.getPoseLandmark(PoseLandmark.LEFT_WRIST));
    double rightelbow = getAngle(
            pose.getPoseLandmark(PoseLandmark.RIGHT_SHOULDER),
            pose.getPoseLandmark(PoseLandmark.RIGHT_ELBOW),
            pose.getPoseLandmark(PoseLandmark.RIGHT_WRIST));
    double lefthip = getAngle(
            pose.getPoseLandmark(PoseLandmark.LEFT_SHOULDER),
            pose.getPoseLandmark(PoseLandmark.LEFT_HIP),
            pose.getPoseLandmark(PoseLandmark.LEFT_KNEE));
    double leftshoulder = getAngle(
            pose.getPoseLandmark(PoseLandmark.LEFT_ELBOW),
            pose.getPoseLandmark(PoseLandmark.LEFT_SHOULDER),
            pose.getPoseLandmark(PoseLandmark.LEFT_HIP));
    double rightshoulder = getAngle(
            pose.getPoseLandmark(PoseLandmark.RIGHT_ELBOW),
            pose.getPoseLandmark(PoseLandmark.RIGHT_SHOULDER),
            pose.getPoseLandmark(PoseLandmark.RIGHT_HIP));
 
    Log.d("rightHipAngle => ", Double.valueOf(righthip).toString());
    Log.d("rightkneeAngle => ", Double.valueOf(rightknee).toString());
    Log.d("leftkneeAngle=> ", Double.valueOf(leftknee).toString());
    Log.d("leftelbowAngle  => ", Double.valueOf(leftelbow).toString());
    Log.d("RightelbowAngle  => ", Double.valueOf(rightelbow).toString());
    Log.d("Lefthipangle  => ", Double.valueOf(lefthip).toString());
    Log.d("leftshoulderangle  => ", Double.valueOf(leftshoulder).toString());
    Log.d("rightshoulderangle  => ", Double.valueOf(rightshoulder).toString());
    double[] Features;
    double[][] beta;
    double[][] beta_1;
    Features = new double[]{righthip, lefthip, rightelbow, leftelbow, rightknee, leftknee, rightshoulder, leftshoulder};
    double[] yPo;
    double[] yPo_1;
    double denomEr = 0.0d;
     double denomEr_1 = 0.0d;

int numPoses=5;
int numPoses_1=5;
beta = new double[numPoses][9];
beta_1 = new double[numPoses_1][9];
    double[] Balancing_Side;
    double[] Inverted_Legs_straight_up;
    double[] Reclining_Up_facing;
    double[] Sitting_Normal1;
    double[] Wheel_Up_facing;

    double[] Balancing;
    double[] Inverted;
    double[] Reclining;
    double[] Sitting;
    double[] Wheel;
    Balancing_Side = new double[]{-7.353371359d,-0.077740057d,0.12379757d,-0.049770707000000004d,0.050496852d,-0.026775309d,-0.019801826d,0.013975578999999998d,0.11927047199999999d};
    Inverted_Legs_straight_up = new double[]{-52.07581979d,0.802024141d,-1.8204475569999998d,-2.418708926d,-2.550124689d,0.458585535d,-6.2515385839999995d,12.83002245d,-0.272565561d};
    Reclining_Up_facing = new double[]{-182.8291691d,2.9138495360000003d,0.442196456d,0.098790503d,0.463574648d,-1.900559243d,-6.68369895d,2.22059342d,-1.423695811d};
    Sitting_Normal1 = new double[]{54.81999148d,-0.08807964800000001d,-0.216165092d,-0.023816729d,0.015954201d,-0.28760509100000003d,-0.130013831d,0.287929255d,-0.315370857d};
    Wheel_Up_facing = new double[]{-169.72565780000002d,0.125218437d,0.560552297d,0.023981336000000002d,0.25020061899999996d,-0.15151456800000002d,0.229740904d,0.32902629d,0.068231069d};
    Balancing = new double[]{-7.353371359d,-0.077740057d,0.12379757d,-0.049770707000000004d,0.050496852d,-0.026775309d,-0.019801826d,0.013975578999999998d,0.11927047199999999d};
    Inverted = new double[]{-52.07581979d,0.802024141d,-1.8204475569999998d,-2.418708926d,-2.550124689d,0.458585535d,-6.2515385839999995d,12.83002245d,-0.272565561d};
    Reclining = new double[]{-182.8291691d,2.9138495360000003d,0.442196456d,0.098790503d,0.463574648d,-1.900559243d,-6.68369895d,2.22059342d,-1.423695811d};
    Sitting = new double[]{54.81999148d,-0.08807964800000001d,-0.216165092d,-0.023816729d,0.015954201d,-0.28760509100000003d,-0.130013831d,0.287929255d,-0.315370857d};
    Wheel = new double[]{-169.72565780000002d,0.125218437d,0.560552297d,0.023981336000000002d,0.25020061899999996d,-0.15151456800000002d,0.229740904d,0.32902629d,0.068231069d};

//Densify the beta matrix
for (int i = 0; i <= Balancing_Side.length - 1; i++)
{
      beta[0][i] = Balancing_Side[i];
      beta[1][i] = Inverted_Legs_straight_up[i];
      beta[2][i] = Reclining_Up_facing[i];
      beta[3][i] = Sitting_Normal1[i];
      beta[4][i] = Wheel_Up_facing[i];

}

//Densify the beta_1 matrix
for (int i = 0; i <= Balancing.length - 1; i++)
{
      beta_1[0][i] = Balancing[i];
      beta_1[1][i] = Inverted[i];
      beta_1[2][i] = Reclining[i];
      beta_1[3][i] = Sitting[i];
      beta_1[4][i] = Wheel[i];

}

    yPo = new double[numPoses + 1];
yPo[0] = beta[0][0];
yPo[1] = beta[1][0];
yPo[2] = beta[2][0];
yPo[3] = beta[3][0];
yPo[4] = beta[4][0];
for (int i = 1; i <= Balancing_Side.length - 1; i++)
{
  yPo[0] = yPo[0] + beta[0][i] * Features[i-1];
  yPo[1] = yPo[1] + beta[1][i] * Features[i-1];
  yPo[2] = yPo[2] + beta[2][i] * Features[i-1];
  yPo[3] = yPo[3] + beta[3][i] * Features[i-1];
  yPo[4] = yPo[4] + beta[4][i] * Features[i-1];

}
    yPo_1 = new double[numPoses_1 + 1];
yPo_1[0] = beta_1[0][0];
yPo_1[1] = beta_1[1][0];
yPo_1[2] = beta_1[2][0];
yPo_1[3] = beta_1[3][0];
yPo_1[4] = beta_1[4][0];
for (int i = 1; i <= Balancing.length - 1; i++)
{
  yPo_1[0] = yPo_1[0] + beta_1[0][i] * Features[i-1];
  yPo_1[1] = yPo_1[1] + beta_1[1][i] * Features[i-1];
  yPo_1[2] = yPo_1[2] + beta_1[2][i] * Features[i-1];
  yPo_1[3] = yPo_1[3] + beta_1[3][i] * Features[i-1];
  yPo_1[4] = yPo_1[4] + beta_1[4][i] * Features[i-1];

}
double[] zPo = new double[]{yPo[0],yPo[1],yPo[2],yPo[3],yPo[4]};
double[] numEr = new double[]{0.0d,0.0d,0.0d,0.0d,0.0d};
double[] softMax = new double[]{0.0d,0.0d,0.0d,0.0d,0.0d};

double[] zPo_1 = new double[]{yPo_1[0],yPo_1[1],yPo_1[2],yPo_1[3],yPo_1[4]};
double[] numEr_1 = new double[]{0.0d,0.0d,0.0d,0.0d,0.0d};
double[] softMax_1 = new double[]{0.0d,0.0d,0.0d,0.0d,0.0d};

    for (int i = 0; i <= numPoses - 1; i++) {
      numEr[i] = Math.exp(zPo[i]);
      denomEr = denomEr + Math.exp(zPo[i]);


    }
    for (int i = 0; i <= numPoses - 1; i++) {
      softMax[i] = numEr[i] / denomEr;

    }
    int maxPos = 0;
    double maxSoftmax = softMax[0];
    for (int i = 1; i <= numPoses - 1; i++) {
      if (softMax[i] > maxSoftmax) {
        maxSoftmax = softMax[i];
        maxPos = i;
      }

    }
    for (int i = 0; i <= numPoses_1 - 1; i++) {
      numEr_1[i] = Math.exp(zPo_1[i]);
      denomEr_1 = denomEr_1 + Math.exp(zPo_1[i]);


    }
    for (int i = 0; i <= numPoses_1 - 1; i++) {
      softMax_1[i] = numEr_1[i] / denomEr_1;

    }
    int maxPos_1 = 0;
    double maxSoftmax_1 = softMax_1[0];
    for (int i = 1; i <= numPoses_1 - 1; i++) {
      if (softMax_1[i] > maxSoftmax_1) {
        maxSoftmax_1 = softMax_1[i];
        maxPos_1 = i;
      }

    }
    String pose="no pose";
switch (maxPos + 1) {
      case 1:
          pose="Balancing_Side";
          Log.d("Posename", "This is Balancing_Side");
          break;
      case 2:
          pose="Inverted_Legs_straight_up";
          Log.d("Posename", "This is Inverted_Legs_straight_up");
          break;
      case 3:
          pose="Reclining_Up_facing";
          Log.d("Posename", "This is Reclining_Up_facing");
          break;
      case 4:
          pose="Sitting_Normal1";
          Log.d("Posename", "This is Sitting_Normal1");
          break;
      case 5:
          pose="Wheel_Up_facing";
          Log.d("Posename", "This is Wheel_Up_facing");
          break;
      default:
           Log.d("Posename", "NA");
           break;
}
    String pose_1="no pose";
switch (maxPos_1 + 1) {
      case 1:
          pose_1="Balancing";
          Log.d("Posename_1", "This is Balancing");
          break;
      case 2:
          pose_1="Inverted";
          Log.d("Posename_1", "This is Inverted");
          break;
      case 3:
          pose_1="Reclining";
          Log.d("Posename_1", "This is Reclining");
          break;
      case 4:
          pose_1="Sitting";
          Log.d("Posename_1", "This is Sitting");
          break;
      case 5:
          pose_1="Wheel";
          Log.d("Posename_1", "This is Wheel");
          break;
      default:
           Log.d("Posename_1", "NA");
           break;
}
//////////////////////////
    ///////////////////////////////////////Printing results start

    Paint paint=new Paint();

    paint.setColor(Color.RED);
    paint.setTextSize(40);
    canvas.drawText("Pose_class is:" + pose_1, 10, 25, paint);
    canvas.drawText("Posename:" + pose, 10, 65, paint);
    

///////////////////////////////////////////
///////////////////////////////////printing result send
    //Log.d("anglerange  => ", Double.valueOf(angle1).toString());
    //Log.d("posename  => ", Double.valueOf(poseNamePred).toString());


    Log.d("leftShoulder => ", leftShoulder.getPosition().toString());
    Log.d("rightShoulder => ", rightShoulder.getPosition().toString());
    Log.d("leftElbow => ", leftElbow.getPosition().toString());
    Log.d("rightElbow => ", rightElbow.getPosition().toString());
    Log.d("leftWrist => ", leftWrist.getPosition().toString());
    Log.d("rightWrist => ", rightWrist.getPosition().toString());
    Log.d("leftHip => ", leftHip.getPosition().toString());
    Log.d("rightHip => ", rightHip.getPosition().toString());
    Log.d("leftKnee => ", leftKnee.getPosition().toString());
    Log.d("rightKnee => ", rightKnee.getPosition().toString());
    Log.d("leftAnkle => ", leftAnkle.getPosition().toString());
    Log.d("rightAnkle => ", rightAnkle.getPosition().toString());
    Log.d("leftPinky => ", leftPinky.getPosition().toString());
    Log.d("rightPinky => ", rightPinky.getPosition().toString());
    Log.d("leftIndex => ", leftIndex.getPosition().toString());
    Log.d("rightIndex => ", rightIndex.getPosition().toString());
    Log.d("leftThumb => ", leftThumb.getPosition().toString());
    Log.d("rightThumb => ", rightThumb.getPosition().toString());
    Log.d("leftHeel => ", leftHeel.getPosition().toString());
    Log.d("rightHeel => ", rightHeel.getPosition().toString());
    Log.d("leftFootIndex => ", leftFootIndex.getPosition().toString());
    Log.d("rightFootIndex => ", rightFootIndex.getPosition().toString());

    drawLine(canvas, leftShoulder.getPosition(), rightShoulder.getPosition(), whitePaint);
    drawLine(canvas, leftHip.getPosition(), rightHip.getPosition(), whitePaint);

    // Left body
    drawLine(canvas, leftShoulder.getPosition(), leftElbow.getPosition(), leftPaint);
    drawLine(canvas, leftElbow.getPosition(), leftWrist.getPosition(), leftPaint);
    drawLine(canvas, leftShoulder.getPosition(), leftHip.getPosition(), leftPaint);
    drawLine(canvas, leftHip.getPosition(), leftKnee.getPosition(), leftPaint);
    drawLine(canvas, leftKnee.getPosition(), leftAnkle.getPosition(), leftPaint);
    drawLine(canvas, leftWrist.getPosition(), leftThumb.getPosition(), leftPaint);
    drawLine(canvas, leftWrist.getPosition(), leftPinky.getPosition(), leftPaint);
    drawLine(canvas, leftWrist.getPosition(), leftIndex.getPosition(), leftPaint);
    drawLine(canvas, leftAnkle.getPosition(), leftHeel.getPosition(), leftPaint);
    drawLine(canvas, leftHeel.getPosition(), leftFootIndex.getPosition(), leftPaint);

    // Right body
    drawLine(canvas, rightShoulder.getPosition(), rightElbow.getPosition(), rightPaint);
    drawLine(canvas, rightElbow.getPosition(), rightWrist.getPosition(), rightPaint);
    drawLine(canvas, rightShoulder.getPosition(), rightHip.getPosition(), rightPaint);
    drawLine(canvas, rightHip.getPosition(), rightKnee.getPosition(), rightPaint);
    drawLine(canvas, rightKnee.getPosition(), rightAnkle.getPosition(), rightPaint);
    drawLine(canvas, rightWrist.getPosition(), rightThumb.getPosition(), rightPaint);
    drawLine(canvas, rightWrist.getPosition(), rightPinky.getPosition(), rightPaint);
    drawLine(canvas, rightWrist.getPosition(), rightIndex.getPosition(), rightPaint);
    drawLine(canvas, rightAnkle.getPosition(), rightHeel.getPosition(), rightPaint);
    drawLine(canvas, rightHeel.getPosition(), rightFootIndex.getPosition(), rightPaint);
  }


  void drawPoint(Canvas canvas, @Nullable PointF point, Paint paint) {
    if (point == null) {
      return;
    }
    canvas.drawCircle(translateX(point.x), translateY(point.y), DOT_RADIUS, paint);
  }

  void drawLine(Canvas canvas, @Nullable PointF start, @Nullable PointF end, Paint paint) {
    if (start == null || end == null) {
      return;
    }
    canvas.drawLine(
            translateX(start.x), translateY(start.y), translateX(end.x), translateY(end.y), paint);
  }

  // Find angles
  static double getAngle(PoseLandmark firstPoint, PoseLandmark midPoint, PoseLandmark lastPoint) {
    double result =
            Math.toDegrees(
                    Math.atan2(lastPoint.getPosition().y - midPoint.getPosition().y,
                            lastPoint.getPosition().x - midPoint.getPosition().x)
                            - Math.atan2(firstPoint.getPosition().y - midPoint.getPosition().y,
                            firstPoint.getPosition().x - midPoint.getPosition().x));
    result = Math.abs(result); // Angle should never be negative
    if (result > 180) {
      result = (360.0 - result); // Always get the acute representation of the angle
    }
    return result;
  }
}