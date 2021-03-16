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
    Features = new double[]{righthip, lefthip, rightelbow, leftelbow, rightknee, leftknee, rightshoulder, leftshoulder};
    double[] yPo;
    double denomEr = 0.0d;

int numPoses=6;
beta = new double[numPoses][9];
    double[] Balancing_Side;
    double[] Inverted_Legs_straight_up;
    double[] Reclining_Up_facing;
    double[] Sitting_Normal1;
    double[] Sitting_Twist;
    double[] Wheel_Up_facing;
    Balancing_Side = new double[]{-7.3533713585184d,-0.0777400568888453d,0.12379757042318801d,-0.0497707066983981d,0.0504968520836324d,-0.0267753090485155d,-0.0198018256433829d,0.0139755786237901d,0.119270472406685d};
    Inverted_Legs_straight_up = new double[]{-52.07581979250939d,0.8020241405169d,-1.8204475568516298d,-2.4187089262676604d,-2.55012468912375d,0.45858553546448105d,-6.25153858384331d,12.8300224535655d,-0.272565560668309d};
    Reclining_Up_facing = new double[]{-182.82916914115899d,2.91384953619889d,0.442196455539185d,0.0987905033971645d,0.46357464778933005d,-1.90055924258005d,-6.68369895002328d,2.2205934195133303d,-1.42369581076253d};
    Sitting_Normal1 = new double[]{54.81999147649611d,-0.0880796483456031d,-0.21616509216056698d,-0.0238167291664289d,0.0159542005137475d,-0.287605090917635d,-0.130013831117185d,0.287929255252889d,-0.31537085664753495d};
    Sitting_Twist = new double[]{-293.94614855751803d,-4.05894326748367d,-2.4685569546148d,-3.3047012940879603d,6.14359240746938d,-4.26401135090281d,-0.972127106894521d,15.538110454694701d,-0.45100924159091205d};
    Wheel_Up_facing = new double[]{-169.725657788262d,0.12521843712857597d,0.560552296769792d,0.0239813360532979d,0.250200619240543d,-0.151514568458917d,0.22974090361170002d,0.32902628988104904d,0.0682310690897684d};

//Densify the beta matrix
for (int i = 0; i <= Balancing_Side.length - 1; i++)
{
      beta[0][i] = Balancing_Side[i];
      beta[1][i] = Inverted_Legs_straight_up[i];
      beta[2][i] = Reclining_Up_facing[i];
      beta[3][i] = Sitting_Normal1[i];
      beta[4][i] = Sitting_Twist[i];
      beta[5][i] = Wheel_Up_facing[i];

}

    yPo = new double[numPoses + 1];
yPo[0] = beta[0][0];
yPo[1] = beta[1][0];
yPo[2] = beta[2][0];
yPo[3] = beta[3][0];
yPo[4] = beta[4][0];
yPo[5] = beta[5][0];
for (int i = 1; i <= Balancing_Side.length - 1; i++)
{
  yPo[0] = yPo[0] + beta[0][i] * Features[i-1];
  yPo[1] = yPo[1] + beta[1][i] * Features[i-1];
  yPo[2] = yPo[2] + beta[2][i] * Features[i-1];
  yPo[3] = yPo[3] + beta[3][i] * Features[i-1];
  yPo[4] = yPo[4] + beta[4][i] * Features[i-1];
  yPo[5] = yPo[5] + beta[5][i] * Features[i-1];

}
double[] zPo = new double[]{yPo[0],yPo[1],yPo[2],yPo[3],yPo[4],yPo[5]};
double[] numEr = new double[]{0.0d,0.0d,0.0d,0.0d,0.0d,0.0d};
double[] softMax = new double[]{0.0d,0.0d,0.0d,0.0d,0.0d,0.0d};

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
          pose="Sitting_Twist";
          Log.d("Posename", "This is Sitting_Twist");
          break;
      case 6:
          pose="Wheel_Up_facing";
          Log.d("Posename", "This is Wheel_Up_facing");
          break;
      default:
           Log.d("Posename", "NA");
           break;
}
//////////////////////////
    ///////////////////////////////////////Printing results start

    Paint paint=new Paint();

    paint.setColor(Color.RED);
    paint.setTextSize(40);
    //canvas.drawText("Angle is:" + angle1, 10, 25, paint);
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